using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TopoRough
{
    public class GlobalVariables
    {
        public static Panel ActivePanel { get; set; } = null;
        public static string ActiveMenuSection
        {
            get
            {
                return activeMenuSection;
            }
            set
            {
                activeMenuSection = value;
            }
        }

        private static string activeMenuSection = "homePanel";
    }
}
