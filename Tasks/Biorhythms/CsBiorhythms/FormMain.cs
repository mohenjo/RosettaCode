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
        private const int VIEW_DAYS_SPAN = 20; // 바이오리듬 차트를 나타낼 범위. 기준일 +/- SPAN

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
            InitDateSelection();
            InitChart();
        }

        private void buttonShowChart_Click(object sender, EventArgs e)
        {
            int dayDiff = (int)Math.Ceiling((dateTimePickerCheckDay.Value - dateTimePickerBirthday.Value).TotalDays);
            if (dayDiff < VIEW_DAYS_SPAN)
            {
                MessageBox.Show($"확인 날짜와 생일 간에는 {VIEW_DAYS_SPAN}일 이상의 차이가 있어야 합니다.", "날짜 입력 오류", MessageBoxButtons.OK);
                InitDateSelection();
            }

            this.Birthday = dateTimePickerBirthday.Value;
            this.CheckDay = dateTimePickerCheckDay.Value;
            GenerateDateSet();
            InitChart();
            DrawChart();

            // 디버그 출력
            Biorhythm bio = new Biorhythm(this.Birthday, this.CheckDay);
            Debug.WriteLine($"\nDays elapsed: {bio.DaysElapsed:#,##0}");
            Dictionary<Biorhythm.BioType, double> bioResult = bio.GetBiorhytms();
            Debug.WriteLine($"신체: {bioResult[Biorhythm.BioType.Physical]:f1}%");
            Debug.WriteLine($"감성: {bioResult[Biorhythm.BioType.Emotional]:f1}%");
            Debug.WriteLine($"지성: {bioResult[Biorhythm.BioType.Mental]:f1}%");
        }

        /// <summary>
        /// 날짜 선택을 초기화
        /// </summary>
        private void InitDateSelection()
        {
            dateTimePickerCheckDay.Value = dateTimePickerBirthday.Value.AddDays(VIEW_DAYS_SPAN);
        }

        /// <summary>
        /// 바이오리듬 차트를 초기화
        /// </summary>
        private void InitChart()
        {
            chartBiorhythms.ChartAreas.Clear();
            chartBiorhythms.Series.Clear();
        }

        /// <summary>
        /// 차트 작성을 위한 데이터 세트 초기화
        /// </summary>
        private void GenerateDateSet()
        {
            this.SeriesX = new List<string>();
            this.SeriesY = new List<Dictionary<Biorhythm.BioType, double>>();
            for (int daysDiff = -VIEW_DAYS_SPAN; daysDiff <= VIEW_DAYS_SPAN; daysDiff++)
            {
                var currentDay = CheckDay.AddDays(daysDiff);
                SeriesX.Add(currentDay.ToString("yy-MM-dd"));
                var bioOfcurrentDay = new Biorhythm(this.Birthday, currentDay);
                SeriesY.Add(bioOfcurrentDay.GetBiorhytms());
            }
        }

        private void DrawChart()
        {
            chartBiorhythms.ChartAreas.Add("Biorhythms");

            chartBiorhythms.ChartAreas["Biorhythms"].AxisX.Interval = 1;
            chartBiorhythms.ChartAreas["Biorhythms"].AxisY.Minimum = -100;
            chartBiorhythms.ChartAreas["Biorhythms"].AxisY.Maximum = 100;
            chartBiorhythms.ChartAreas["Biorhythms"].AxisY.Interval = 10;

            chartBiorhythms.ChartAreas["Biorhythms"].AxisX.Title = "Date";
            chartBiorhythms.ChartAreas["Biorhythms"].AxisY.Title = "Biorhythms(%)";

            chartBiorhythms.Series.Add("Physical");
            chartBiorhythms.Series.Add("Emotional");
            chartBiorhythms.Series.Add("Mental");


            chartBiorhythms.Series["Physical"].ChartArea = "Biorhythms";
            chartBiorhythms.Series["Emotional"].ChartArea = "Biorhythms";
            chartBiorhythms.Series["Mental"].ChartArea = "Biorhythms";

            chartBiorhythms.Series["Physical"].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Spline;
            chartBiorhythms.Series["Emotional"].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Spline;
            chartBiorhythms.Series["Mental"].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Spline;
            chartBiorhythms.Series["Physical"].BorderWidth = 2;
            chartBiorhythms.Series["Emotional"].BorderWidth = 2;
            chartBiorhythms.Series["Mental"].BorderWidth = 2;

            chartBiorhythms.Series["Physical"].Points.Clear();
            for (int idx = 0; idx < this.SeriesX.Count; idx++)
            {
                chartBiorhythms.Series["Physical"].Points.
                    AddXY(this.SeriesX[idx],
                    this.SeriesY[idx][Biorhythm.BioType.Physical]);
                chartBiorhythms.Series["Emotional"].Points.AddY(this.SeriesY[idx][Biorhythm.BioType.Emotional]);
                chartBiorhythms.Series["Mental"].Points.AddY(this.SeriesY[idx][Biorhythm.BioType.Mental]);
            }
        }
    }
}
