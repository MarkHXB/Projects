using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using TopoRough.Models;


namespace TopoRough.Models
{
    public class MenuItem
    {
        public MenuItem(PictureBox _icon, string _title)
        {
            this.Icon = _icon;
            this.Title = _title;
        }

        public static List<MenuItem> List { get; set; } = new List<MenuItem>();
        public PictureBox Icon { get; set;  }
        public string Title { get; set;  }
    }
}
