##
# Created by: Curtis Szmania
# Date: 6/5/2017
# Initial Creation.
###

from logging import getLogger
from .lib import Lib
from os import path

__author__ = 'szmania'

FFMPEG_LOG = 'ffmpeg.log'
SCRIPT_DIR = path.dirname(path.realpath(__file__))

class FFMPEG_Lib(object):
    def __init__(self, ffmpegExePath, logLevel='DEBUG', logFilePath=FFMPEG_LOG):
        """
        Library for __ffmpeg converter and encoder interaction.

<<<<<<< HEAD
        Args:
            ffmpegExePath (str): Path to ffmpeg.exe
            logLevel (str): Logging level setting ie: "DEBUG" or "WARN"
=======
        :param ffmpegExePath: Path to __ffmpeg.exe
        :type ffmpegExePath: String.
        :param logLevel: Logging level setting ie: "DEBUG" or "WARN"
        :type logLevel: String.
>>>>>>> b35cd581f1b922abdb239ce8e6e4edd74ffb48cd
        """

        self.__ffmpegExePath = ffmpegExePath
        self.__logLevel = logLevel
        self.__ffmpegLog = logFilePath

        self.__lib = Lib(logLevel=logLevel)


    def compress_video_file(self, filePath, targetPath):
        """
        Compress video file.

        Args:
            filePath (str): File path of video to __compressAll.
            targetPath (str): File path of video to be compressed into.

        Returns:
            subprocess object:
        """
    
        logger = getLogger('ffmpeg.compress_video_file')
        logger.setLevel(self.__logLevel)
    
        logger.debug(' Compressing video file: "%s"' % filePath)
    
        cmd = '"%s" -i "%s" -vf "scale=\'if(gte(iw,720), 720, iw)\':-2" -preset medium -threads 1 "%s"' % \
              (self.__ffmpegExePath, filePath, targetPath)
    
        logger = getLogger('__lib.compress_video_file')
        logger.setLevel(self.logLevel)
    
        logger.debug(' Compressing video file: "%s"' % filePath)
    
        cmd = '"%s" -i "%s" -vf "scale=\'if(gte(iw,720), 720, iw)\':-2" -preset medium -__threads 1 "%s"' % (self.ffmpegExePath, filePath, targetPath)
    
        proc1 = self._exec_cmd(command=cmd, noWindow=True)
    
        return proc1

        result = self.__lib.exec_cmd(command=cmd, noWindow=True, outputFile=self.__ffmpegLog)

        if result:
            logger.debug(' Success, could compress video file "%s" to "%s".' % (filePath, targetPath))
        else:
            logger.error(' Error, could NOT compress video file "%s"!' % filePath)
        return result
