// Totally hacky tool to split files out of the SL.LNK file
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <memory.h>
#include <assert.h>
#include <sys/stat.h>
#include <algorithm>
#include <vector>

#define MAX_SIZE	(2*1024*1024)

struct BigEndWord
{
	void		Set(uint32_t value)
	{
		m_bytes[0] = (value >> 24) & 0xff;
		m_bytes[1] = (value >> 16) & 0xff;
		m_bytes[2] = (value >> 8) & 0xff;
		m_bytes[3] = (value >> 0) & 0xff;
	}
	uint8_t		m_bytes[4];	
} __attribute__ ((packed));

struct BigEndShort
{
	void		Set(uint32_t value)
	{
		m_bytes[0] = (value >> 8) & 0xff;
		m_bytes[1] = (value >> 0) & 0xff;
	}
	uint8_t		m_bytes[2];	
} __attribute__ ((packed));

struct FileEntry
{
	BigEndWord	m_startOffset;
	char		m_fileName[12];
} __attribute__ ((packed));

int main(int argc, const char** argv)
{
	if (argc <= 1)
	{
		printf("unlinkfile <in files>\n");
		return 1;
	}
	
	// NOTE: all writing has to be in bigendian format
	uint32_t fileCount = argc - 1;
	
	// Pass one: accumulate the sizes and write the header
	
	// The format is
	// 2 bytes -- file count
	// FileEntry * file count
	// 4 bytes -- extra BigEndWord so it knows how big the last file is.
	uint32_t offset = 2 + sizeof(FileEntry) * fileCount + sizeof(BigEndWord);
	
	FILE* pOutput = fopen("SL.LNK", "wb");

	BigEndShort count;
	count.Set(fileCount);
	fwrite(&count, sizeof(count), 1, pOutput);
	
	for (uint i = 0; i < fileCount; ++i)
	{
		FileEntry entry;
		const char* pName = argv[i + 1];
		printf("%s\n", pName);
		
		// Get the file size
		struct stat st;
		if (stat(pName, &st) < 0)
		{
			return 3;
		}
		printf("Offset: %u\n", offset);
		printf("File size: %u\n", st.st_size);
		memset(&entry, 0, sizeof(entry));
		entry.m_startOffset.Set(offset);
		
		// Strip off the path (linux only)
		int c = strlen(pName);
		while (c > 0)
		{
			if (pName[c] == '/')
				break;
			--c;
		}
		// C will now either point to the separator or -1
		++c;
		printf("Truncated filename: %s\n", pName + c);
		
		// Can't use sprintf here -- if the name is 12 chars it inserts a
		// terminator!
		for (unsigned int d = 0; d < sizeof(entry.m_fileName); ++d)
		{
			if (pName[d + c] == 0)
				break;
			entry.m_fileName[d] = pName[d + c];
		}
		fwrite(&entry, sizeof(entry), 1, pOutput);
		offset += st.st_size;
	}
	
	printf("Final offset: %u\n", offset);
	
	// Write the final offset
	BigEndWord finalOffset;
	finalOffset.Set(offset);
	fwrite(&finalOffset, sizeof(finalOffset), 1, pOutput);
	
	// Now copy the file data	
	uint8_t* pData = (uint8_t*) malloc(MAX_SIZE);
	for (uint i = 0; i < fileCount; ++i)
	{
		const char* pName = argv[i + 1];
		FILE* pInfile = fopen(pName, "rb");
		int len = fread(pData, 1, MAX_SIZE, pInfile);
		fclose(pInfile);
		printf("File size; %u\n", len);
		(void) fwrite(pData, 1, len, pOutput);
	}

	fclose(pOutput);
	return 0;
}

