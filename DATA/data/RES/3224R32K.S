* ###########################################################################
* #                                                                         #
* #  'ScreensPain' coded 1993 by Chris of AURA & Scandion of the Mugwumps  #
* #                                                                         #
* #                 --- It's an INDEPENDENT-Product ---                     #
* #                                                                         #
* ###########################################################################
* Monitor: RGB/TV
* 320*240, True Color, 50.0 Hz, 15625 Hz

        MOVE.L   #$FE00CC,$FFFF8282.W
        MOVE.L   #$280039,$FFFF8286.W
        MOVE.L   #$9A00D9,$FFFF828A.W
        MOVE.L   #$2710265,$FFFF82A2.W
        MOVE.L   #$590059,$FFFF82A6.W
        MOVE.L   #$239026B,$FFFF82AA.W
        MOVE.W   #$200,$FFFF820A.W
        MOVE.W   #$181,$FFFF82C0.W
        CLR.W    $FFFF8266.W
        MOVE.W   #$100,$FFFF8266.W
        MOVE.W   #$0,$FFFF82C2.W
        MOVE.W   #$140,$FFFF8210.W
