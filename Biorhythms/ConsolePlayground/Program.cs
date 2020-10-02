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

            Console.WriteLine($"Days elapsed: {bio.DaysElapsed:#,##0}");
            Dictionary<Biorhythm.BioType, double> bioResult = bio.GetBiorhytms();
            Console.WriteLine($"신체: {bioResult[Biorhythm.BioType.Physical]:f1}%");
            Console.WriteLine($"감성: {bioResult[Biorhythm.BioType.Emotional]:f1}%");
            Console.WriteLine($"지성: {bioResult[Biorhythm.BioType.Mental]:f1}%");
        }
    }
}
