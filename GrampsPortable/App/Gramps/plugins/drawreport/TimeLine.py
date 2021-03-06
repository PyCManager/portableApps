#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2003-2007 Donald N. Allingham
# Copyright (C) 2007-2008 Brian G. Matherly
# Copyright (C) 2010       Jakim Friant
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
Timeline Chart
"""

#------------------------------------------------------------------------
#
# python modules
#
#------------------------------------------------------------------------
from gen.ggettext import sgettext as _

#------------------------------------------------------------------------
#
# GRAMPS modules
#
#------------------------------------------------------------------------
from gen.plug.menu import PersonOption, FilterOption, EnumeratedListOption
from gen.plug.report import Report
from gen.plug.report import utils as ReportUtils
from gen.plug.report import MenuReportOptions
pt2cm = ReportUtils.pt2cm
from gen.plug.docgen import (FontStyle, ParagraphStyle, GraphicsStyle,
                    FONT_SANS_SERIF, DASHED, PARA_ALIGN_CENTER)
import Sort
from gen.display.name import displayer as name_displayer
import config
from gen.utils import get_birth_or_fallback, get_death_or_fallback

#------------------------------------------------------------------------
#
# private constants
#
#------------------------------------------------------------------------ 
cal = config.get('preferences.calendar-format-report')

#------------------------------------------------------------------------
#
# Private Functions
#
#------------------------------------------------------------------------
def _get_sort_functions(sort):
    return [
        (_("Birth Date"),sort.by_birthdate_key),
        (_("Name"),sort.by_last_name_key), 
]

#------------------------------------------------------------------------
#
# TimeLine
#
#------------------------------------------------------------------------
class TimeLine(Report):

    def __init__(self, database, options, user):
        """
        Create the Timeline object that produces the report.
        
        The arguments are:

        database        - the GRAMPS database instance
        options         - instance of the Options class for this report
        user            - instance of gen.user.User()

        This report needs the following parameters (class variables)
        that come in the options class.
        
        filter    - Filter to be applied to the people of the database.
                    The option class carries its number, and the function
                    returning the list of filters.
        sortby -    Sorting method to be used.
        """
        Report.__init__(self, database, options, user)
        self._user = user
        menu = options.menu
        self.filter = menu.get_option_by_name('filter').get_filter()

        sort_func_num = menu.get_option_by_name('sortby').get_value()
        sort_functions = _get_sort_functions(Sort.Sort(database))
        self.sort_name = sort_functions[sort_func_num][0]
        self.sort_func = sort_functions[sort_func_num][1]
        self.calendar = config.get('preferences.calendar-format-report')

    def write_report(self):
        # Apply the filter
        self._user.begin_progress(_('Timeline'), 
                                  _('Applying filter...'), 
                                  self.database.get_number_of_people())
        self.plist = self.filter.apply(self.database, 
                                       self.database.iter_person_handles(),
                                       self._user.step_progress)
        self._user.end_progress()

        # Find the range of dates to include
        (low, high) = self.find_year_range()
        
        # Generate the actual timeline
        self.generate_timeline(low, high)

    def generate_timeline(self, low, high):
        st_size = self.name_size()
        style_sheet = self.doc.get_style_sheet()
        font = style_sheet.get_paragraph_style('TLG-Name').get_font()
        incr = pt2cm(font.get_size())
        pad =  incr * 0.75
        x1,x2,y1,y2 = (0, 0, 0, 0)
        start = st_size + 0.5
        stop = self.doc.get_usable_width() - 0.5
        size = (stop - start)
        self.header = 2.0
        
        # Sort the people as requested
        self._user.begin_progress(_('Timeline'), _('Sorting dates...'), 0)
        self.plist.sort(key=self.sort_func)
        self._user.end_progress()
        
        self.doc.start_page()
        self.build_grid(low, high, start, stop)

        index = 1
        current = 1;

        length = len(self.plist)
        
        self._user.begin_progress(_('Timeline'), 
                                  _('Calculating timeline...'), length)

        for p_id in self.plist:
            p = self.database.get_person_from_handle(p_id)
            birth = get_birth_or_fallback(self.database, p)
            if birth:
                b = birth.get_date_object().to_calendar(self.calendar).get_year()
            else:
                b = None

            death = get_death_or_fallback(self.database, p)
            if death:
                d = death.get_date_object().to_calendar(self.calendar).get_year()
            else:
                d = None

            n = name_displayer.display_formal(p)
            self.doc.draw_text('TLG-text', n,incr+pad,
                               self.header + (incr+pad)*index)
            
            y1 = self.header + (pad+incr)*index
            y2 = self.header + ((pad+incr)*index)+incr
            y3 = (y1+y2)/2.0
            w = 0.05
            
            if b:
                start_offset = ((float(b-low)/float(high-low)) * (size))
                x1 = start+start_offset
                path = [(x1,y1),(x1+w,y3),(x1,y2),(x1-w,y3)]
                self.doc.draw_path('TLG-line',path)

            if d:
                start_offset = ((float(d-low)/float(high-low)) * (size))
                x1 = start+start_offset
                path = [(x1,y1),(x1+w,y3),(x1,y2),(x1-w,y3)]
                self.doc.draw_path('TLG-solid',path)

            if b and d:
                start_offset = ((float(b-low)/float(high-low)) * size) + w
                stop_offset = ((float(d-low)/float(high-low)) * size) - w

                x1 = start+start_offset
                x2 = start+stop_offset
                self.doc.draw_line('open',x1,y3,x2,y3)

            if (y2 + incr) >= self.doc.get_usable_height():
                if current != length:
                    self.doc.end_page()
                    self.doc.start_page()
                    self.build_grid(low, high,start,stop)
                index = 1
                x1,x2,y1,y2 = (0,0,0,0)
            else:
                index += 1;
            current += 1
            self._user.step_progress()
        self.doc.end_page()
        self._user.end_progress()    

    def build_grid(self, year_low, year_high, start_pos, stop_pos):
        """
        Draws the grid outline for the chart. Sets the document label,
        draws the vertical lines, and adds the year labels. Arguments
        are:

        year_low  - lowest year on the chart
        year_high - highest year on the chart
        start_pos - x position of the lowest leftmost grid line
        stop_pos  - x position of the rightmost grid line
        """
        self.draw_title()
        self.draw_columns(start_pos, stop_pos)
        if year_high is not None and year_low is not None:
            self.draw_year_headings(year_low, year_high, start_pos, stop_pos)
        else:
            self.draw_no_date_heading()

    def draw_columns(self, start_pos, stop_pos):
        """
        Draws the columns out of vertical lines.

        start_pos - x position of the lowest leftmost grid line
        stop_pos  - x position of the rightmost grid line
        """
        top_y = self.header
        bottom_y = self.doc.get_usable_height()
        delta = (stop_pos - start_pos)/ 5
        for val in range(0,6):
            xpos = start_pos + (val * delta)
            self.doc.draw_line('TLG-grid', xpos, top_y, xpos, bottom_y)
            
    def draw_title(self):
        """
        Draws the title for the page.
        """
        width = self.doc.get_usable_width()
        # feature request 2356: avoid genitive form
        byline = _("Sorted by %s") % self.sort_name
        # feature request 2356: avoid genitive form
        title = _("Timeline Graph for %s") % self.filter.get_name()
        self.doc.center_text('TLG-title', title + "\n" + byline, width / 2.0, 0)
        
    def draw_year_headings(self, year_low, year_high, start_pos, stop_pos):
        """
        Draws the column headings (years) for the page.
        """
        style_sheet = self.doc.get_style_sheet()
        label_font = style_sheet.get_paragraph_style('TLG-Label').get_font()
        label_y = self.header - (pt2cm(label_font.get_size()) * 1.2)
        top_y = self.header
        bottom_y = self.doc.get_usable_height()
        incr = (year_high - year_low)/5
        delta = (stop_pos - start_pos)/ 5
        for val in range(0,6):
            xpos = start_pos+(val*delta)
            year_str = str(year_low + (incr*val))
            self.doc.center_text('TLG-label', year_str, xpos, label_y)
            
    def draw_no_date_heading(self):
        """
        Draws a single heading that says "No Date Information"
        """
        width = self.doc.get_usable_width()
        style_sheet = self.doc.get_style_sheet()
        label_font = style_sheet.get_paragraph_style('TLG-Label').get_font()
        label_y = self.header - (pt2cm(label_font.get_size()) * 1.2)
        self.doc.center_text('TLG-label', _("No Date Information"),
                             width / 2.0, label_y)

    def find_year_range(self):
        """
        Finds the range of years that will be displayed on the chart.

        Returns a tuple of low and high years. If no dates are found, the
        function returns (None, None).
        """
        low  = None
        high = None

        def min_max_year(low, high, year):
            if year is not None and year != 0:
                if low is not None:
                    low = min(low, year)
                else:
                    low = year
                if high is not None:
                    high = max(high, year)
                else:
                    high = year
            return (low, high)
        
        self._user.begin_progress(_('Timeline'), 
                                  _('Finding date range...'), 
                                  len(self.plist))

        for p_id in self.plist:
            p = self.database.get_person_from_handle(p_id)
            birth = get_birth_or_fallback(self.database, p)
            if birth:
                b = birth.get_date_object().to_calendar(self.calendar).get_year()
                (low, high) = min_max_year(low, high, b)

            death = get_death_or_fallback(self.database, p)
            if death:
                d = death.get_date_object().to_calendar(self.calendar).get_year()
                (low, high) = min_max_year(low, high, d)
            self._user.step_progress()

        # round the dates to the nearest decade
        if low is not None:
            low = int((low/10))*10
        else:
            low = high
            
        if high is not None:
            high = int(((high+9)/10))*10
        else:
            high = low
        
        # Make sure the difference is a multiple of 50 so all year ranges land
        # on a decade.
        if low is not None and high is not None:
            low -= 50 - ((high-low) % 50)
        
        self._user.end_progress()
        return (low, high)

    def name_size(self):
        self.plist = self.filter.apply(self.database,
                                       self.database.iter_person_handles())

        style_sheet = self.doc.get_style_sheet()
        gstyle = style_sheet.get_draw_style('TLG-text')
        pname = gstyle.get_paragraph_style()
        pstyle = style_sheet.get_paragraph_style(pname)
        font = pstyle.get_font()
        
        size = 0
        for p_id in self.plist:
            p = self.database.get_person_from_handle(p_id)
            n = name_displayer.display_formal(p)
            size = max(self.doc.string_width(font, n),size)
        return pt2cm(size)

#------------------------------------------------------------------------
#
# TimeLineOptions
#
#------------------------------------------------------------------------
class TimeLineOptions(MenuReportOptions):

    def __init__(self, name, dbase):
        self.__pid = None
        self.__filter = None
        self.__db = dbase
        MenuReportOptions.__init__(self, name, dbase)
        
    def add_menu_options(self, menu):
        category_name = _("Report Options")

        self.__filter = FilterOption(_("Filter"), 0)
        self.__filter.set_help(
                         _("Determines what people are included in the report"))
        menu.add_option(category_name, "filter", self.__filter)
        self.__filter.connect('value-changed', self.__filter_changed)
        
        self.__pid = PersonOption(_("Filter Person"))
        self.__pid.set_help(_("The center person for the filter"))
        menu.add_option(category_name, "pid", self.__pid)
        self.__pid.connect('value-changed', self.__update_filters)

        self.__update_filters()
        
        sortby = EnumeratedListOption(_('Sort by'), 0 )
        idx = 0
        for item in _get_sort_functions(Sort.Sort(self.__db)):
            sortby.add_item(idx,item[0])
            idx += 1
        sortby.set_help( _("Sorting method to use"))
        menu.add_option(category_name,"sortby",sortby)
                
    def __update_filters(self):
        """
        Update the filter list based on the selected person
        """
        gid = self.__pid.get_value()
        person = self.__db.get_person_from_gramps_id(gid)
        filter_list = ReportUtils.get_person_filters(person, False)
        self.__filter.set_filters(filter_list)
        
    def __filter_changed(self):
        """
        Handle filter change. If the filter is not specific to a person,
        disable the person option
        """
        filter_value = self.__filter.get_value()
        if filter_value in [1, 2, 3, 4]:
            # Filters 1, 2, 3 and 4 rely on the center person
            self.__pid.set_available(True)
        else:
            # The rest don't
            self.__pid.set_available(False)
        
    def make_default_style(self,default_style):
        """Make the default output style for the Timeline report."""
        # Paragraph Styles
        f = FontStyle()
        f.set_size(10)
        f.set_type_face(FONT_SANS_SERIF)
        p = ParagraphStyle()
        p.set_font(f)
        p.set_description(_("The style used for the person's name."))
        default_style.add_paragraph_style("TLG-Name",p)

        f = FontStyle()
        f.set_size(8)
        f.set_type_face(FONT_SANS_SERIF)
        p = ParagraphStyle()
        p.set_font(f)
        p.set_alignment(PARA_ALIGN_CENTER)
        p.set_description(_("The style used for the year labels."))
        default_style.add_paragraph_style("TLG-Label",p)

        f = FontStyle()
        f.set_size(14)
        f.set_type_face(FONT_SANS_SERIF)
        p = ParagraphStyle()
        p.set_font(f)
        p.set_alignment(PARA_ALIGN_CENTER)
        p.set_description(_("The style used for the title of the page."))
        default_style.add_paragraph_style("TLG-Title",p)
        
        """
        Graphic Styles
            TLG-grid  - 0.5pt wide line dashed line. Used for the lines that 
                        make up the grid.
            TLG-line  - 0.5pt wide line. Used for the line connecting two 
                        endpoints and for the birth marker.
            TLG-solid - 0.5pt line with a black fill color. Used for the date of
                        death marker.
            TLG-text  - Contains the TLG-Name paragraph style used for the 
                        individual's name.
            TLG-title - Contains the TLG-Title paragraph style used for the
                        title of the document.
            TLG-label - Contains the TLG-Label paragraph style used for the year
                        label's in the document.
        """
        g = GraphicsStyle()
        g.set_line_width(0.5)
        g.set_color((0,0,0))
        default_style.add_draw_style("TLG-line",g)

        g = GraphicsStyle()
        g.set_line_width(0.5)
        g.set_color((0,0,0))
        g.set_fill_color((0,0,0))
        default_style.add_draw_style("TLG-solid",g)

        g = GraphicsStyle()
        g.set_line_width(0.5)
        g.set_color((0,0,0))
        g.set_fill_color((255,255,255))
        default_style.add_draw_style("open",g)

        g = GraphicsStyle()
        g.set_line_width(0.5)
        g.set_line_style(DASHED)
        g.set_color((0,0,0))
        default_style.add_draw_style("TLG-grid",g)

        g = GraphicsStyle()
        g.set_paragraph_style("TLG-Name")
        g.set_color((0,0,0))
        g.set_fill_color((255,255,255))
        g.set_line_width(0)
        default_style.add_draw_style("TLG-text",g)

        g = GraphicsStyle()
        g.set_paragraph_style("TLG-Title")
        g.set_color((0,0,0))
        g.set_fill_color((255,255,255))
        g.set_line_width(0)
        default_style.add_draw_style("TLG-title",g)

        g = GraphicsStyle()
        g.set_paragraph_style("TLG-Label")
        g.set_color((0,0,0))
        g.set_fill_color((255,255,255))
        g.set_line_width(0)
        default_style.add_draw_style("TLG-label",g)
