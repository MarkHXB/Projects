using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace TopoRough.Constants
{
    public class PictureBoxes
    {
        public static PictureBox SaveButton = new PictureBox()
        {
            Name="saveButton",
            ImageLocation = @"C:\Users\bakon\source\repos\TopoRough\TopoRough\Assets\Icons\save-regular.png",
            Size = new Size(40, 40),
            SizeMode=PictureBoxSizeMode.CenterImage,
        };
    }
}
