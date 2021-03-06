#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2010  Benny Malengier
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
# Standard Python modules
#
#-------------------------------------------------------------------------
from gen.ggettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from Filters.Rules import MatchesFilterBase

#-------------------------------------------------------------------------
#
# MatchesEventFilter
#
#-------------------------------------------------------------------------
class MatchesEventFilterBase(MatchesFilterBase):
    """
    Rule that checks against another filter.

    This is a base rule for subclassing by specific objects.
    Subclasses need to define the namespace class attribute.
    
    """

    labels      = [_('Event filter name:')]
    name        = _('Objects with events matching the <event filter>')
    description = _("Matches objects who have events that match a certain"
                    " event filter")
    category    = _('General filters')

    # we want to have this filter show event filters
    namespace   = 'Event'

    def prepare(self, db):
        MatchesFilterBase.prepare(self, db)
        self.MEF_filt = self.find_filter()    

    def apply(self, db, object):
        if self.MEF_filt is None :
            return False
        
        eventlist = [x.ref for x in object.get_event_ref_list()]
        for eventhandle in eventlist:
            #check if event in event filter
            if self.MEF_filt.check(db, eventhandle):
                return True
        return False
