#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2011       Helge Herz
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
from Filters.Rules import Rule

#-------------------------------------------------------------------------
# "Repositories having a name that contain a substring"
#-------------------------------------------------------------------------
class MatchesNameSubstringOf(Rule):
    """Repository name containing <substring>"""

    labels      = [ _('Text:')]
    name        = _('Repositories with name containing <text>')
    description = _("Matches repositories whose name contains a certain substring")
    category    = _('General filters')
    allow_regex = True

    def apply(self, db, repository):
        """ Apply the filter """
        return self.match_substring(0, repository.get_name())
