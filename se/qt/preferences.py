#!/usr/bin/env python
# Unit Name: preferences
# Created By: Virgil Dupras
# Created On: 2009-05-24
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)

from dupeguru.scanner import SCAN_TYPE_FILENAME, SCAN_TYPE_CONTENT

from base.preferences import Preferences as PreferencesBase

class Preferences(PreferencesBase):
    # (width, is_visible)
    COLUMNS_DEFAULT_ATTRS = [ 
        (200, True), # name
        (180, True), # path
        (60, True), # size
        (40, False), # Kind
        (120, False), # creation
        (120, False), # modification
        (60, True), # match %
        (120, False), # Words Used
        (80, False), # dupe count
    ]
    
    def _load_specific(self, settings, get):
        self.scan_type = get('ScanType', self.scan_type)
        self.word_weighting = get('WordWeighting', self.word_weighting)
        self.match_similar = get('MatchSimilar', self.match_similar)
        self.ignore_small_files = get('IgnoreSmallFiles', self.ignore_small_files)
        self.small_file_threshold = get('SmallFileThreshold', self.small_file_threshold)
    
    def _reset_specific(self):
        self.filter_hardness = 80
        self.scan_type = SCAN_TYPE_CONTENT
        self.word_weighting = True
        self.match_similar = False
        self.ignore_small_files = True
        self.small_file_threshold = 10 # KB
    
    def _save_specific(self, settings, set_):
        set_('ScanType', self.scan_type)
        set_('WordWeighting', self.word_weighting)
        set_('MatchSimilar', self.match_similar)
        set_('IgnoreSmallFiles', self.ignore_small_files)
        set_('SmallFileThreshold', self.small_file_threshold)
    