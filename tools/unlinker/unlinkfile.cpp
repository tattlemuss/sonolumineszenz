// Totally hacky tool to split files out of the SL.LNK file
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <vector>

#define MAX_SIZE	(2*1024*1024)

struct BigEndWord
{
	uint32_t	Get() const
	{
		return (m_bytes[0] << 24) |
			(m_bytes[1] << 16) |
			(m_bytes[2] << 8) |
			(m_bytes[3] << 0);
	}
	uint8_t		m_bytes[4];	
};
struct FileEntry
{
	BigEndWord	m_startOffset;
	char		m_fileName[12];
};

uint16_t ReadWord(const uint8_t*& pData)
{
	uint16_t byte1 = *pData++;
	uint16_t byte2 = *pData++;
	return (byte1 << 8) | (byte2);	
}

int Unpack(const uint8_t* pData)
{
	const uint8_t* pFileBase = pData;
	
	uint16_t numFiles = ReadWord(pData);
	const FileEntry* pEntry = (const FileEntry*) pData;
	for (uint16_t i = 0; i < numFiles; ++i)
	{
		uint32_t thisOffset = pEntry[0].m_startOffset.Get();
		uint32_t nextOffset = pEntry[1].m_startOffset.Get();
		uint32_t size = nextOffset - thisOffset;
		printf("Name: %s Start: %08u (Packed) size: %08d\n", pEntry->m_fileName, thisOffset, size);
				
		// Extract the file
        	char buf[128];
		const uint8_t* pData = pFileBase + thisOffset;
		sprintf(buf, "PAK/%s", pEntry->m_fileName);
		FILE* pOut = fopen(buf, "w");
		if (!pOut)
			return -1;
		fwrite(pData, 1, size, pOut);
		fclose(pOut);
		++pEntry;
	}
	return 0;
	
}
int main(int argc, char** argv)
{
	if (argc <= 1)
	{
		printf("unlinkfile <infile>\n");
		return 1;
	}
	FILE* pInfile = fopen(argv[1], "rb");
	if (!pInfile)
	{
		printf("Can't read file\n");
		return 1;
	}

	uint8_t* pData = (uint8_t*) malloc(MAX_SIZE);
	(void) fread(pData, 1, MAX_SIZE, pInfile);
	fclose(pInfile);
	int ret = Unpack(pData);
	printf("\nCompleted with error code %d\n", ret);
	free(pData);
	return ret;
}

