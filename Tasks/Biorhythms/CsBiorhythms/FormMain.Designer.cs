namespace CsBiorhythms
{
    partial class FormMain
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.dateTimePickerBirthday = new System.Windows.Forms.DateTimePicker();
            this.label2 = new System.Windows.Forms.Label();
            this.dateTimePickerCheckDay = new System.Windows.Forms.DateTimePicker();
            this.buttonShowChart = new System.Windows.Forms.Button();
            this.chartBiorhythms = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.chartBiorhythms)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(109, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "생일을 선택하세요:";
            // 
            // dateTimePickerBirthday
            // 
            this.dateTimePickerBirthday.Location = new System.Drawing.Point(127, 14);
            this.dateTimePickerBirthday.Name = "dateTimePickerBirthday";
            this.dateTimePickerBirthday.Size = new System.Drawing.Size(200, 21);
            this.dateTimePickerBirthday.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 48);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(237, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "바이오리듬을 확인할 기준일을 선택하세요:";
            // 
            // dateTimePickerCheckDay
            // 
            this.dateTimePickerCheckDay.Location = new System.Drawing.Point(255, 42);
            this.dateTimePickerCheckDay.Name = "dateTimePickerCheckDay";
            this.dateTimePickerCheckDay.Size = new System.Drawing.Size(200, 21);
            this.dateTimePickerCheckDay.TabIndex = 4;
            // 
            // buttonShowChart
            // 
            this.buttonShowChart.Location = new System.Drawing.Point(699, 14);
            this.buttonShowChart.Name = "buttonShowChart";
            this.buttonShowChart.Size = new System.Drawing.Size(89, 49);
            this.buttonShowChart.TabIndex = 5;
            this.buttonShowChart.Text = "바이오리듬\r\n확인";
            this.buttonShowChart.UseVisualStyleBackColor = true;
            this.buttonShowChart.Click += new System.EventHandler(this.buttonShowChart_Click);
            // 
            // chartBiorhythms
            // 
            chartArea1.Name = "ChartArea1";
            this.chartBiorhythms.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chartBiorhythms.Legends.Add(legend1);
            this.chartBiorhythms.Location = new System.Drawing.Point(12, 80);
            this.chartBiorhythms.Name = "chartBiorhythms";
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chartBiorhythms.Series.Add(series1);
            this.chartBiorhythms.Size = new System.Drawing.Size(774, 358);
            this.chartBiorhythms.TabIndex = 6;
            this.chartBiorhythms.Text = "chart1";
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.chartBiorhythms);
            this.Controls.Add(this.buttonShowChart);
            this.Controls.Add(this.dateTimePickerCheckDay);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.dateTimePickerBirthday);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormMain";
            this.Text = "Biorhythms - Rosetta Code";
            ((System.ComponentModel.ISupportInitialize)(this.chartBiorhythms)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DateTimePicker dateTimePickerBirthday;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.DateTimePicker dateTimePickerCheckDay;
        private System.Windows.Forms.Button buttonShowChart;
        private System.Windows.Forms.DataVisualization.Charting.Chart chartBiorhythms;
    }
}

