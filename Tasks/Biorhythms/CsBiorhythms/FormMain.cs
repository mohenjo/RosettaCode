using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace CsBiorhythms
{
    public partial class FormMain : Form
    {
        private const int VIEW_DAYS_SPAN = 40; // 바이오리듬 차트를 나타낼 범위(일)

        private List<string> SeriesX = new List<string>();

        private List<Dictionary<Biorhythm.BioType, double>> SeriesY = new List<Dictionary<Biorhythm.BioType, double>>();

        public FormMain()
        {
            InitializeComponent();
            Initialize(); // 윈폼 프로젝트를 초기화/개인화
        }


        public DateTime Birthday { get; private set; }

        public DateTime CheckDay { get; private set; }

        private void Initialize()
        {
            InitDaySelection();
            InitChar();
        }

        private void buttonShowChart_Click(object sender, EventArgs e)
        {
            var dayDiff = dateTimePickerCheckDay.Value - dateTimePickerBirthday.Value;
            Debug.WriteLine(dayDiff);
            if (dayDiff.Days < VIEW_DAYS_SPAN /2)
            {
                MessageBox.Show($"확인 날짜와 생일 간에는 {VIEW_DAYS_SPAN / 2}이상의 차이(일)가 있어야 합니다.", "날짜 입력 오류", MessageBoxButtons.OK);
                InitDaySelection();
            }
            this.Birthday = dateTimePickerBirthday.Value;
            this.CheckDay = dateTimePickerCheckDay.Value;
            InitChar();
            InitDateSet();
        }

        private void InitDaySelection()
        {
            dateTimePickerCheckDay.Value = dateTimePickerBirthday.Value.AddDays(VIEW_DAYS_SPAN / 2);
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
            this.SeriesX = new List<string>();
            this.SeriesY = new List<Dictionary<Biorhythm.BioType, double>>();
            for (int daysDiff = -VIEW_DAYS_SPAN/2; daysDiff <= VIEW_DAYS_SPAN /2; daysDiff++)
            {
                var currentDay = CheckDay.AddDays(daysDiff);
                SeriesX.Add(currentDay.ToString("yy-MM-dd"));
                var bioOfcurrentDay = new Biorhythm(this.Birthday, currentDay);
                SeriesY.Add(bioOfcurrentDay.GetBiorhytms());
            }
            
        }
    }
}
