using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsBiorhythms
{
    public class Biorhythm
    {

        public Biorhythm(DateTime birthday, DateTime checkday)
        {
            this.Birthday = birthday;
            this.CheckDay = checkday;

            DaysElapsed = (checkday - birthday).Days;
            if (DaysElapsed < 15)
            {
                throw new ArgumentException("생일과 최소 15일 이상 차이나는 날짜를 체크해야 합니다.");
            }


        }

        public DateTime Birthday { get; private set; }

        public DateTime CheckDay { get; private set; }

        public int DaysElapsed { get; private set; }
    }
}
