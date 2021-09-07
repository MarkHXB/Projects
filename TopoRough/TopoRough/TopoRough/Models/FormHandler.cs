using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TopoRough.Models
{
    public interface IFormHandler
    {
        void SwitchForm(Form currentForm, object newForm,string switchToName);
    }
    public class FormHandler:IFormHandler
    {
        public Form PreviousPage { get; set; }

        public void SwitchForm(Form currentForm, object newForm,string switchToName)
        {
            currentForm.Hide();
 
            try
            {
                if (PreviousPage != null)
                {
                    Form form = Application.OpenForms[PreviousPage.Name];
                    form.Show();
                }
                else
                {
                    Form form = (Form)newForm;
                    if (form is not null)
                    {
                        form.Show();
                    }
                }

                GlobalVariables.ActiveMenuSection = $"{switchToName}";
            }
            catch (Exception x)
            {
                MessageBox.Show(x.Message);
            }
            finally
            {
                PreviousPage = currentForm;
            }
        }
    }
}
