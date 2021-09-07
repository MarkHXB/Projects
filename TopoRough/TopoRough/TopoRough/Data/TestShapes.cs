using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Drawing;
using System.IO;

namespace TopoRough.Data
{
    public class TestShapes
    {
        public int Id { get; set; }
        public PictureBox Item { get; set; }
        public string Title { get; set; }
        public static List<TestShapes> Shapes = FillShapeList();

        public static List<string> FolderExam()
        {
            List<string>FileNames = new List<string>();

            try
            {
                string[] fileEntries = Directory.GetFiles(@"C:\Users\bakon\source\repos\TopoRough\TopoRough\Assets\Shapes\");
                foreach (string fileName in fileEntries)
                    FileNames.Add(ProcessFile(fileName));
            }
            catch (Exception x)
            {
                Console.WriteLine(x.Message);
            }

            return FileNames;
        }
        private static string ProcessFile(string path)
        {
            string result = Path.GetFileName(path);
            return result;
        }
        public static List<TestShapes> FillShapeList()
        {
            List<string> fileNames = FolderExam();
            List<TestShapes> shapes = new List<TestShapes>();

            int counter = 0;

            foreach (var file in fileNames)
            {
                shapes.Add(new TestShapes
                {
                    Id = counter,
                    Item = new PictureBox()
                    {
                        ImageLocation = $@"C:\Users\bakon\source\repos\TopoRough\TopoRough\Assets\Shapes\{file}",
                        SizeMode = PictureBoxSizeMode.Zoom,
                        Name = $"{file}Shape",
                        Size = new Size(90, 90),
                    }
                });

                counter++;
            }

            return shapes;
        }
    }
}
