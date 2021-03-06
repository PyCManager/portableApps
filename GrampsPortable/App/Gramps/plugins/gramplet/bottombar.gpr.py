#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2011 Nick Hall
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

#------------------------------------------------------------------------
#
# Register Gramplet
#
#------------------------------------------------------------------------
register(GRAMPLET, 
         id="Person Details", 
         name=_("Person Details"), 
         description = _("Gramplet showing details of a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="PersonDetails.py",
         height=200,
         gramplet = 'PersonDetails',
         gramplet_title=_("Details"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Repository Details", 
         name=_("Repository Details"), 
         description = _("Gramplet showing details of a repository"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="RepositoryDetails.py",
         height=200,
         gramplet = 'RepositoryDetails',
         gramplet_title=_("Details"),
         navtypes=["Repository"],
         )

register(GRAMPLET, 
         id="Place Details", 
         name=_("Place Details"), 
         description = _("Gramplet showing details of a place"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="PlaceDetails.py",
         height=200,
         gramplet = 'PlaceDetails',
         gramplet_title=_("Details"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Media Preview", 
         name=_("Media Preview"), 
         description = _("Gramplet showing a preview of a media object"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="MediaPreview.py",
         height=200,
         gramplet = 'MediaPreview',
         gramplet_title=_("Preview"),
         navtypes=["Media"],
         )

try:
    import pyexiv2
    available = True
except:
    import logging
    logging.warning(_("WARNING: pyexiv2 module not loaded.  "
                      "Image metadata functionality will not be available."))
    available = False

if available:
    register(GRAMPLET, 
            id = "Metadata Viewer", 
            name = _("Metadata Viewer"), 
            description = _("Gramplet showing metadata for a media object"),
            version = "1.0.0",
            gramps_target_version = "3.4",
            status = STABLE,
            fname = "MetadataViewer.py",
            height = 200,
            gramplet = 'MetadataViewer',
            gramplet_title = _("Image Metadata"),
            navtypes=["Media"],
            )

register(GRAMPLET, 
         id="Person Residence", 
         name=_("Person Residence"), 
         description = _("Gramplet showing residence events for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="PersonResidence.py",
         height=200,
         gramplet = 'PersonResidence',
         gramplet_title=_("Residence"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Person Events", 
         name=_("Person Events"), 
         description = _("Gramplet showing the events for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Events.py",
         height=200,
         gramplet = 'PersonEvents',
         gramplet_title=_("Events"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Family Events", 
         name=_("Family Events"), 
         description = _("Gramplet showing the events for a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Events.py",
         height=200,
         gramplet = 'FamilyEvents',
         gramplet_title=_("Events"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Person Gallery", 
         name=_("Person Gallery"), 
         description = _("Gramplet showing media objects for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'PersonGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Family Gallery", 
         name=_("Family Gallery"), 
         description = _("Gramplet showing media objects for a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'FamilyGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Event Gallery", 
         name=_("Event Gallery"), 
         description = _("Gramplet showing media objects for an event"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'EventGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Place Gallery", 
         name=_("Place Gallery"), 
         description = _("Gramplet showing media objects for a place"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'PlaceGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Source Gallery", 
         name=_("Source Gallery"), 
         description = _("Gramplet showing media objects for a source"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'SourceGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Source"],
         )

register(GRAMPLET, 
         id="Citation Gallery", 
         name=_("Citation Gallery"), 
         description = _("Gramplet showing media objects for a citation"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Gallery.py",
         height=200,
         gramplet = 'CitationGallery',
         gramplet_title=_("Gallery"),
         navtypes=["Citation"],
         )

register(GRAMPLET, 
         id="Person Attributes", 
         name=_("Person Attributes"), 
         description = _("Gramplet showing the attributes of a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Attributes.py",
         height=200,
         gramplet = 'PersonAttributes',
         gramplet_title=_("Attributes"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Event Attributes", 
         name=_("Event Attributes"), 
         description = _("Gramplet showing the attributes of an event"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Attributes.py",
         height=200,
         gramplet = 'EventAttributes',
         gramplet_title=_("Attributes"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Family Attributes", 
         name=_("Family Attributes"), 
         description = _("Gramplet showing the attributes of a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Attributes.py",
         height=200,
         gramplet = 'FamilyAttributes',
         gramplet_title=_("Attributes"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Media Attributes", 
         name=_("Media Attributes"), 
         description = _("Gramplet showing the attributes of a media object"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Attributes.py",
         height=200,
         gramplet = 'MediaAttributes',
         gramplet_title=_("Attributes"),
         navtypes=["Media"],
         )

register(GRAMPLET, 
         id="Person Notes", 
         name=_("Person Notes"), 
         description = _("Gramplet showing the notes for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'PersonNotes',
         gramplet_title=_("Notes"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Event Notes", 
         name=_("Event Notes"), 
         description = _("Gramplet showing the notes for an event"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'EventNotes',
         gramplet_title=_("Notes"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Family Notes", 
         name=_("Family Notes"), 
         description = _("Gramplet showing the notes for a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'FamilyNotes',
         gramplet_title=_("Notes"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Place Notes", 
         name=_("Place Notes"), 
         description = _("Gramplet showing the notes for a place"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'PlaceNotes',
         gramplet_title=_("Notes"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Source Notes", 
         name=_("Source Notes"), 
         description = _("Gramplet showing the notes for a source"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'SourceNotes',
         gramplet_title=_("Notes"),
         navtypes=["Source"],
         )

register(GRAMPLET, 
         id="Citation Notes", 
         name=_("Citation Notes"), 
         description = _("Gramplet showing the notes for a citation"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'CitationNotes',
         gramplet_title=_("Notes"),
         navtypes=["Citation"],
         )

register(GRAMPLET, 
         id="Repository Notes", 
         name=_("Repository Notes"), 
         description = _("Gramplet showing the notes for a repository"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'RepositoryNotes',
         gramplet_title=_("Notes"),
         navtypes=["Repository"],
         )

register(GRAMPLET, 
         id="Media Notes", 
         name=_("Media Notes"), 
         description = _("Gramplet showing the notes for a media object"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Notes.py",
         height=200,
         gramplet = 'MediaNotes',
         gramplet_title=_("Notes"),
         navtypes=["Media"],
         )

register(GRAMPLET, 
         id="Person Citations", 
         name=_("Person Citations"), 
         description = _("Gramplet showing the citations for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Citations.py",
         height=200,
         gramplet = 'PersonCitations',
         gramplet_title=_("Citations"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Event Citations", 
         name=_("Event Citations"), 
         description = _("Gramplet showing the citations for an event"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Citations.py",
         height=200,
         gramplet = 'EventCitations',
         gramplet_title=_("Citations"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Family Citations", 
         name=_("Family Citations"), 
         description = _("Gramplet showing the citations for a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Citations.py",
         height=200,
         gramplet = 'FamilyCitations',
         gramplet_title=_("Citations"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Place Citations", 
         name=_("Place Citations"), 
         description = _("Gramplet showing the citations for a place"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Citations.py",
         height=200,
         gramplet = 'PlaceCitations',
         gramplet_title=_("Citations"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Media Citations", 
         name=_("Media Citations"), 
         description = _("Gramplet showing the citations for a media object"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Citations.py",
         height=200,
         gramplet = 'MediaCitations',
         gramplet_title=_("Citations"),
         navtypes=["Media"],
         )

register(GRAMPLET, 
         id="Person Children", 
         name=_("Person Children"), 
         description = _("Gramplet showing the children of a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Children.py",
         height=200,
         gramplet = 'PersonChildren',
         gramplet_title=_("Children"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Family Children", 
         name=_("Family Children"), 
         description = _("Gramplet showing the children of a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Children.py",
         height=200,
         gramplet = 'FamilyChildren',
         gramplet_title=_("Children"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Person Backlinks", 
         name=_("Person Backlinks"), 
         description = _("Gramplet showing the backlinks for a person"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'PersonBacklinks',
         gramplet_title=_("References"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Event Backlinks", 
         name=_("Event Backlinks"), 
         description = _("Gramplet showing the backlinks for an event"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'EventBacklinks',
         gramplet_title=_("References"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Family Backlinks", 
         name=_("Family Backlinks"), 
         description = _("Gramplet showing the backlinks for a family"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'FamilyBacklinks',
         gramplet_title=_("References"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Place Backlinks", 
         name=_("Place Backlinks"), 
         description = _("Gramplet showing the backlinks for a place"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'PlaceBacklinks',
         gramplet_title=_("References"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Source Backlinks", 
         name=_("Source Backlinks"), 
         description = _("Gramplet showing the backlinks for a source"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'SourceBacklinks',
         gramplet_title=_("References"),
         navtypes=["Source"],
         )

register(GRAMPLET, 
         id="Citation Backlinks", 
         name=_("Citation Backlinks"), 
         description = _("Gramplet showing the backlinks for a citation"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'CitationBacklinks',
         gramplet_title=_("References"),
         navtypes=["Citation"],
         )

register(GRAMPLET, 
         id="Repository Backlinks", 
         name=_("Repository Backlinks"), 
         description = _("Gramplet showing the backlinks for a repository"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'RepositoryBacklinks',
         gramplet_title=_("References"),
         navtypes=["Repository"],
         )

register(GRAMPLET, 
         id="Media Backlinks", 
         name=_("Media Backlinks"), 
         description = _("Gramplet showing the backlinks for a media object"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'MediaBacklinks',
         gramplet_title=_("References"),
         navtypes=["Media"],
         )

register(GRAMPLET, 
         id="Note Backlinks", 
         name=_("Note Backlinks"), 
         description = _("Gramplet showing the backlinks for a note"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Backlinks.py",
         height=200,
         gramplet = 'NoteBacklinks',
         gramplet_title=_("References"),
         navtypes=["Note"],
         )

register(GRAMPLET, 
         id="Person Filter", 
         name=_("Person Filter"), 
         description = _("Gramplet providing a person filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'PersonFilter',
         gramplet_title=_("Filter"),
         navtypes=["Person"],
         )

register(GRAMPLET, 
         id="Family Filter", 
         name=_("Family Filter"), 
         description = _("Gramplet providing a family filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'FamilyFilter',
         gramplet_title=_("Filter"),
         navtypes=["Family"],
         )

register(GRAMPLET, 
         id="Event Filter", 
         name=_("Event Filter"), 
         description = _("Gramplet providing an event filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'EventFilter',
         gramplet_title=_("Filter"),
         navtypes=["Event"],
         )

register(GRAMPLET, 
         id="Source Filter", 
         name=_("Source Filter"), 
         description = _("Gramplet providing a source filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'SourceFilter',
         gramplet_title=_("Filter"),
         navtypes=["Source"],
         )

register(GRAMPLET, 
         id="Citation Filter", 
         name=_("Citation Filter"), 
         description = _("Gramplet providing a citation filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'CitationFilter',
         gramplet_title=_("Filter"),
         navtypes=["Citation"],
         )

register(GRAMPLET, 
         id="Place Filter", 
         name=_("Place Filter"), 
         description = _("Gramplet providing a place filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'PlaceFilter',
         gramplet_title=_("Filter"),
         navtypes=["Place"],
         )

register(GRAMPLET, 
         id="Media Filter", 
         name=_("Media Filter"), 
         description = _("Gramplet providing a media filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'MediaFilter',
         gramplet_title=_("Filter"),
         navtypes=["Media"],
         )

register(GRAMPLET, 
         id="Repository Filter", 
         name=_("Repository Filter"), 
         description = _("Gramplet providing a repository filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'RepositoryFilter',
         gramplet_title=_("Filter"),
         navtypes=["Repository"],
         )

register(GRAMPLET, 
         id="Note Filter", 
         name=_("Note Filter"), 
         description = _("Gramplet providing a note filter"),
         version="1.0.0",
         gramps_target_version="3.4",
         status = STABLE,
         fname="Filter.py",
         height=200,
         gramplet = 'NoteFilter',
         gramplet_title=_("Filter"),
         navtypes=["Note"],
         )
