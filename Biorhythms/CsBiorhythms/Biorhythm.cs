using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsBiorhythms
{
    public class Biorhythm
    {
        /// <summary>
        /// 바이오리듬 객체를 생성합니다.
        /// </summary>
        /// <param name="birthday">생일</param>
        /// <param name="checkday">바이오리듬을 확인할 날짜</param>
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

        /// <summary>
        /// 생일
        /// </summary>
        public DateTime Birthday { get; private set; }

        /// <summary>
        /// 바이오리듬을 확인할 날짜
        /// </summary>
        public DateTime CheckDay { get; private set; }

        /// <summary>
        /// 생일로부터 바이오리듬 확인일까지의 경과일 수
        /// </summary>
        public int DaysElapsed { get; private set; }

        /// <summary>
        /// 바이오리듬 값을 반환합니다.
        /// </summary>
        /// <param name="circle">신체(23), 감성(28), 지성(33)에 대한 주기 수</param>
        /// <param name="daysElapsced">경과일수</param>
        /// <returns></returns>
        private static double GetBiovalue(int circle, int daysElapsced)
            => Math.Sin(2 * Math.PI * daysElapsced / circle) * 100;

        /// <summary>
        /// 신체에 대한 바이오리듬 값을 계산합니다.
        /// </summary>
        /// <param name="daysElapsed"></param>
        /// <returns></returns>
        public static double GetPhysicalValue(int daysElapsed)
            => GetBiovalue(23, daysElapsed);

        /// <summary>
        /// 감성에 대한 바이오리듬 값을 계산합니다.
        /// </summary>
        /// <param name="daysElapsed"></param>
        /// <returns></returns>
        public static double GetEmotionalValue(int daysElapsed)
            => GetBiovalue(28, daysElapsed);

        /// <summary>
        /// 지성에 대한 바이오리듬 값을 계산합니다.
        /// </summary>
        /// <param name="daysElapsed"></param>
        /// <returns></returns>
        public static double GetMentalvalue(int daysElapsed)
            => GetBiovalue(33, daysElapsed);
    }
}
