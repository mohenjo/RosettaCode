using System;
using System.Collections.Generic;
using System.Linq;

namespace CsSolution
{
    class Program
    {
        static void Main()
        {
            List<int> rst = GetSolution();
            Console.WriteLine($"{rst[0]}^5 + {rst[1]}^5 + {rst[2]}^5 + {rst[3]}^5 = {rst[4]}^5");
            Console.ReadKey();
            // 27 ^ 5 + 84 ^ 5 + 110 ^ 5 + 133 ^ 5 = 144 ^ 5
        }

        static List<int> GetSolution()
        {
            int maxLimit = 250;

            List<long> poweredPool = Enumerable.Range(0, maxLimit)
                .Select(n => (long)Math.Pow(n, 5)).ToList();

            Dictionary<long, int> poweredPool2y = Enumerable.Range(0, maxLimit)
                .ToDictionary(n => (long)Math.Pow(n, 5), n => n);

            for (int x0 = 1; x0 < maxLimit; x0++)
            {
                Console.WriteLine($"Processing {x0} within range (0..{maxLimit})");
                for (int x1 = x0; x1 < maxLimit; x1++)
                {
                    for (int x2 = x1; x2 < maxLimit; x2++)
                    {
                        for (int x3 = x2; x3 < maxLimit; x3++)
                        {
                            List<int> foo = new List<int> { x0, x1, x2, x3 };
                            long summation = foo.Select(x => poweredPool[x]).Sum();
                            if (poweredPool2y.ContainsKey(summation))
                            {
                                int y = poweredPool2y[summation];
                                if (!foo.Contains(y))
                                {
                                    foo.Add(y);
                                    return foo;
                                }
                            }
                        }
                    }
                }
            }
            return null;
        }
    }
}
