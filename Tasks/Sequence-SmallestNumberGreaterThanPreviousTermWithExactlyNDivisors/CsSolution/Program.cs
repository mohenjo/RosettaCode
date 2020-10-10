using System;
using System.Collections.Generic;
using System.Linq;

namespace CsSolution
{
    class Program
    {
        static void Main()
        {
            int loopCount = 15;
            foreach (var item in GenerateSeries().Take(loopCount))
            {
                Console.WriteLine(item);
            }
        }

        static IEnumerable<int> GenerateSeries()
        {
            int curIdx = 1;
            int curVal = 1;
            while (true)
            {
                if (GetDivisorsCount(curVal) == curIdx)
                {
                    curIdx++;
                    yield return curVal;
                }
                curVal++;
            }
        }


        static int GetDivisorsCount(int aNumber)
        {
            HashSet<int> divisors = new HashSet<int>();
            for (int n = 1; n * n <= aNumber; n++)
            {
                int quo = Math.DivRem(aNumber, n, out int rem);
                if (rem == 0)
                {
                    divisors.Add(n);
                    divisors.Add(quo);
                }
            }
            return divisors.Count;
        }
    }
}
