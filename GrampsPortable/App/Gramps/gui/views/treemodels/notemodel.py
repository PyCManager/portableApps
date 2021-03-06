#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2007  Donald N. Allingham
# Copyright (C) 2010       Nick Hall
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

#-------------------------------------------------------------------------
#
# python modules
#
#-------------------------------------------------------------------------
import logging
_LOG = logging.getLogger(".gui.notemodel")
import locale

#-------------------------------------------------------------------------
#
# GNOME/GTK modules
#
#-------------------------------------------------------------------------
import gtk

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
import Utils
from gui.views.treemodels.flatbasemodel import FlatBaseModel
from gen.lib import (Note, NoteType, StyledText)

#-------------------------------------------------------------------------
#
# NoteModel
#
#-------------------------------------------------------------------------
class NoteModel(FlatBaseModel):
    """
    """
    def __init__(self, db, scol=0, order=gtk.SORT_ASCENDING, search=None,
                 skip=set(), sort_map=None):
        """Setup initial values for instance variables."""
        self.gen_cursor = db.get_note_cursor
        self.map = db.get_raw_note_data
        self.fmap = [
            self.column_preview,
            self.column_id,
            self.column_type,
            self.column_tags,
            self.column_change,
            self.column_handle,
            self.column_tag_color
        ]
        self.smap = [
            self.column_preview,
            self.column_id,
            self.column_type,
            self.column_tags,
            self.sort_change,
            self.column_handle,
            self.column_tag_color
        ]
        FlatBaseModel.__init__(self, db, scol, order, search=search,
                           skip=skip, sort_map=sort_map)

    def destroy(self):
        """
        Unset all elements that can prevent garbage collection
        """
        self.db = None
        self.gen_cursor = None
        self.map = None
        self.fmap = None
        self.smap = None
        FlatBaseModel.destroy(self)

    def color_column(self):
        """
        Return the color column.
        """
        return 6

    def on_get_n_columns(self):
        """Return the column number of the Note tab."""
        return len(self.fmap) + 1

    def column_handle(self, data):
        """Return the handle of the Note."""
        return data[Note.POS_HANDLE]

    def column_id(self, data):
        """Return the id of the Note."""
        return unicode(data[Note.POS_ID])

    def column_type(self, data):
        """Return the type of the Note in readable format."""
        temp = NoteType()
        temp.set(data[Note.POS_TYPE])
        return unicode(str(temp))

    def column_preview(self, data):
        """Return a shortend version of the Note's text."""
        #data is the encoding in the database, make it a unicode object
        #for universal work
        note = unicode(data[Note.POS_TEXT][StyledText.POS_TEXT])
        note = " ".join(note.split())
        if len(note) > 80:
            return note[:80] + "..."
        else:
            return note

    def sort_change(self, data):
        return "%012x" % data[Note.POS_CHANGE]
    
    def column_change(self,data):
        return Utils.format_time(data[Note.POS_CHANGE])

    def get_tag_name(self, tag_handle):
        """
        Return the tag name from the given tag handle.
        """
        return self.db.get_tag_from_handle(tag_handle).get_name()
        
    def column_tag_color(self, data):
        """
        Return the tag color.
        """
        tag_color = None
        tag_priority = None
        for handle in data[Note.POS_TAGS]:
            tag = self.db.get_tag_from_handle(handle)
            this_priority = tag.get_priority()
            if tag_priority is None or this_priority < tag_priority:
                tag_color = tag.get_color()
                tag_priority = this_priority
        return tag_color

    def column_tags(self, data):
        """
        Return the sorted list of tags.
        """
        tag_list = map(self.get_tag_name, data[Note.POS_TAGS])
        return ', '.join(sorted(tag_list, key=locale.strxfrm))
