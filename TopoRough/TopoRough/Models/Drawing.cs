using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TopoRough.Models
{
    public interface IDrawing
    {
        void DrawBorder(object sender, PaintEventArgs e);
    }

    public class Drawing : IDrawing
    {
        public void DrawBorder(object sender, PaintEventArgs e)
        {
            Panel panel = (Panel)sender;
            ControlPaint.DrawBorder(e.Graphics, panel.ClientRectangle,
              Color.Black, 3, ButtonBorderStyle.Solid, // left
              Color.Black, 3, ButtonBorderStyle.Solid, // top
              Color.Black, 3, ButtonBorderStyle.Solid, // right
              Color.Black, 3, ButtonBorderStyle.Solid);// bottom
        }
    }
}
