using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CsBiorhythms;

namespace ConsolePlayground
{
    class Program
    {
        static void Main()
        {
            DateTime birthday = new DateTime(1943, 03, 09);
            DateTime checkday = new DateTime(1972, 07, 11);
            Biorhythm bio = new Biorhythm(birthday, checkday);
            

            Console.WriteLine(bio.DaysElapsed);
        }
    }
}
