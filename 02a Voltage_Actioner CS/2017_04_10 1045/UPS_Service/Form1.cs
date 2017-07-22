using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Management.Automation;

namespace UPS_Service
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string tString = string.Empty;
        SerialPort _serialPort = new SerialPort();

        private void Form1_Load(object sender, EventArgs e)
        {
            foreach (string s in SerialPort.GetPortNames())
            {
                comboBox1.Items.Add(s);
            }
            //comboBox1.SelectedIndex = 0;
        }

        void button1_Click(object sender, EventArgs e)
        {
                comboBox1.Visible = false;
                button1.Visible = false;
                button2.Visible = true;

                _serialPort.BaudRate = 9600;
                _serialPort.PortName = comboBox1.Text;
                _serialPort.Open();
                _serialPort.DataReceived += new SerialDataReceivedEventHandler(_serialPort_DataReceived);
                // this.WindowState = FormWindowState.Minimized;
                Main_Resize();
        }

        private void Main_Resize()
        {
            if (FormWindowState.Minimized == this.WindowState)
            {
                mynotifyicon.Visible = true;
                mynotifyicon.ShowBalloonTip(500);
                this.Hide();
            }

            else if (FormWindowState.Normal == this.WindowState)
            {
                mynotifyicon.Visible = false;
            }
        }

        void _serialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            
            byte[] buffer = new byte[1];
            int bytesRead = _serialPort.Read(buffer, 0, buffer.Length);
            tString += Encoding.ASCII.GetString(buffer, 0, bytesRead);
            if (tString == "Z")
            {
            Process ExternalProcess = new Process();
            ExternalProcess.StartInfo.FileName = "shutdown";
            //ExternalProcess.StartInfo.Arguments = "/s /f /t 0";
            ExternalProcess.StartInfo.Arguments = "/s";
            ExternalProcess.StartInfo.WindowStyle = ProcessWindowStyle.Minimized;
            ExternalProcess.Start();
            ExternalProcess.WaitForExit();
            }
            tString = "";
        }

        private void mynotifyIcon_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            Show();
            this.WindowState = FormWindowState.Normal;
            mynotifyicon.Visible = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            _serialPort.Close();
            button2.Visible = false;
            button1.Visible = true;
            comboBox1.Visible = true;
        }

        private void Form1_ResizeEnd(object sender, EventArgs e)
        {
            if (FormWindowState.Minimized == this.WindowState)
            {
                mynotifyicon.Visible = true;
                // mynotifyicon.ShowBalloonTip(500);
                this.Hide();
            }

            else if (FormWindowState.Normal == this.WindowState)
            {
                mynotifyicon.Visible = false;
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            if (FormWindowState.Minimized == this.WindowState)
            {
                mynotifyicon.Visible = true;
                // mynotifyicon.ShowBalloonTip(500);
                this.Hide();
            }

            else if (FormWindowState.Normal == this.WindowState)
            {
                mynotifyicon.Visible = false;
            }
        } 
    }
}
