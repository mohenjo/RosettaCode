using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CsBiorhythms
{
    public partial class FormMain : Form
    {
        private const int VIEW_DAYS_SPAN = 40; // 바이오리듬 차트를 나타낼 범위(일)

        private List<DateTime> SeriesX = new List<DateTime>();

        public FormMain()
        {
            InitializeComponent();
            Initialize(); // 윈폼 프로젝트를 초기화/개인화
        }


        public DateTime Birthday { get; private set; }

        public DateTime CheckDay { get; private set; }

        private void Initialize()
        {
        }

        private void buttonShowChart_Click(object sender, EventArgs e)
        {
            this.Birthday = dateTimePickerBirthday.Value;
            this.CheckDay = dateTimePickerCheckDay.Value;
            InitChar();
        }

        private void InitChar()
        {
            chartBiorhythms.ChartAreas.Clear();
            chartBiorhythms.Series.Clear();

            chartBiorhythms.ChartAreas.Add("Biorhythms");
            chartBiorhythms.ChartAreas["Biorhythms"].AxisX.Minimum = -15;
        }

        private void InitDateSet()
        {
            DateTime BeginDate = CheckDay.AddDays(-VIEW_DAYS_SPAN / 2);
            DateTime EndDate = CheckDay.AddDays(VIEW_DAYS_SPAN / 2);
        }
    }
}
