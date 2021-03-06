#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2007  Donald N. Allingham
# Copyright (C) 2007-2008  Brian G. Matherly
# Copyright (C) 2011       Tim G L Lyons
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

"""
Package providing filter rules for GRAMPS.
"""

from _HasCitation import HasCitation
from _AllCitations import AllCitations
from _ChangedSince import ChangedSince
from _CitationPrivate import CitationPrivate
from _HasGallery import HasGallery
from _HasIdOf import HasIdOf
from _HasNote import HasNote
from _HasNoteMatchingSubstringOf import HasNoteMatchingSubstringOf
from _HasNoteRegexp import HasNoteRegexp
from _HasReferenceCountOf import HasReferenceCountOf
from _HasSource import HasSource
from _HasSourceIdOf import HasSourceIdOf
from _HasSourceNoteRegexp import HasSourceNoteRegexp
from _MatchesFilter import MatchesFilter
from _MatchesPageSubstringOf import MatchesPageSubstringOf
from _MatchesRepositoryFilter import MatchesRepositoryFilter
from _MatchesSourceFilter import MatchesSourceFilter
from _RegExpIdOf import RegExpIdOf
from _RegExpSourceIdOf import RegExpSourceIdOf

editor_rule_list = [
    HasCitation,
    AllCitations,
    ChangedSince,
    CitationPrivate,
    HasGallery,
    HasIdOf,
    HasNote,
    HasNoteRegexp,
    HasReferenceCountOf,
    HasSource,
    HasSourceIdOf,
    HasSourceNoteRegexp,
    MatchesFilter,
    MatchesPageSubstringOf,
    MatchesRepositoryFilter,
    MatchesSourceFilter, 
    RegExpIdOf,
    RegExpSourceIdOf
]
