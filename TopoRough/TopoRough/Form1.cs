using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using TopoRough.Screens;
using TopoRough.Screens.MainScreen;
using TopoRough.Constants;
using TopoRough.Models;

namespace TopoRough
{
    public partial class MainScreen : Form
    {
        private bool drawedBorder = false;

        private float zoom = 1f;

        private bool isEditing = true;
        private bool lastOpenShapes = false;


        //COMPONENTS & INTERFECES
        private Drawing draw = new Drawing();
        private FormHandler formHandler = new FormHandler();

        public MainScreen()
        {
            InitializeComponent();
            EditStatus();
            LoadShapeList.InitList(shapeItemsPanel);
            label1.Text = shapePanel.Controls.Count.ToString();
            pictureBox5.AllowDrop = true;
            sandboxPanel.AllowDrop = true;
        }

        private void Show_On_MainMenu()
        {
            mainMenuPanel.Visible = true;
            savePanel.Visible = true;
            uploadPanel.Visible = true;
            settingsPanel.Visible = true;
            exitPanel.Visible = true;
            shapePanel.Visible = true;
            if (lastOpenShapes)
                shapeItemsPanel.Visible = true;
        }
        private void Show_Off_MainMenu()
        {
            mainMenuPanel.Visible = false;
            savePanel.Visible = false;
            uploadPanel.Visible = false;
            settingsPanel.Visible = false;
            exitPanel.Visible = false;
            shapePanel.Visible = false;
            shapeItemsPanel.Visible = false;
        }

        private void mainMenuBarStatusBtn_Click(object sender, EventArgs e)
        {
            if (mainMenuPanel.Visible == false)
            {
                Show_On_MainMenu();
            }
            else
                Show_Off_MainMenu();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            if (mainMenuPanel.Visible == false)
            {
                Show_On_MainMenu();
            }
            else
                Show_Off_MainMenu();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            if (mainMenuPanel.Visible == false)
            {
                Show_On_MainMenu();
            }
            else
                Show_Off_MainMenu();
        }

        private void EditStatus()
        {
            if (isEditing)
            {
                editableTitle.ForeColor = Color.Green;
                editableTitle.Text = "Munka betöltve";
            }
            else
            {
                editableTitle.ForeColor = Color.BlueViolet;
                editableTitle.Text = "Hozz létre egy új munkát";
            }
        }

        private void editButton_Click(object sender, EventArgs e)
        {
            if (isEditing)
            {

            }
        }

        private void editLink_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            if (isEditing)
            {

            }
        }

        private void shapesOpenCloseButton_Click(object sender, EventArgs e)
        {
            if (isEditing)
            {
                if (shapeItemsPanel.Visible == false)
                {
                    shapeItemsPanel.Visible = true;
                    lastOpenShapes = true;
                }
                else
                {
                    shapeItemsPanel.Visible = false;
                    lastOpenShapes = false;
                }
                    
            }
        }



        private void pictureBox5_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.All;
        }

        private void pictureBox5_DragDrop(object sender, DragEventArgs e)
        {
            ((PictureBox)e.Data.GetData(typeof(PictureBox))).Parent = (Panel)sender;
        }
        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            pictureBox5.DoDragDrop(pictureBox5, DragDropEffects.All);
        }





        private void sandboxPanel_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.All;
        }

        private void sandboxPanel_DragDrop(object sender, DragEventArgs e)
        {
            //((Button)e.Data.GetData(typeof(Button))).Parent = (Panel)sender;
            PictureBox item = (PictureBox)e.Data.GetData(typeof(PictureBox));
            item.Location = new Point(e.X, e.Y);
            sandboxPanel.Controls.Add(item);
        }



        private void pictureBox4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void exitLink_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Application.Exit();
        }

        private void sandboxPanel_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.ScaleTransform(zoom, zoom);
        }

        private void label2_Click(object sender, EventArgs e)
        {
            zoom = 25f;
            sandboxPanel.Invalidate();
        }

        private void settingsLink_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            formHandler.SwitchForm(ActiveForm, new Settings(),"settingsPanel");
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            formHandler.SwitchForm(ActiveForm, new Settings(), "settingsPanel");
        }

        private void uploadLink_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {

        }

        private void homePanel_Paint(object sender, PaintEventArgs e)
        {
            if (GlobalVariables.ActiveMenuSection == "homePanel")
            {
                draw.DrawBorder(sender, e);
            }
        }
    }
}
