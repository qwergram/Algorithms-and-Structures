using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Quicksort
{
    class Quicksort
    {

        static List<int> recursiveQuicksort(List<int> values)
        {
            if (values.Count() > 0)
            {
                var pivot = values[0];
                var smaller = new List<int>();
                var larger = new List<int>();
                for (int i = 1; i < values.Count(); i++)
                {
                    var item = values[i];
                    if (item < pivot)
                    {
                        smaller.Add(item);
                    } else
                    {
                        larger.Add(item);
                    }
                }

                var result = recursiveQuicksort(smaller);
                result.Add(pivot);
                result.AddRange(recursiveQuicksort(larger));

                return result;

            }
            return values;
        }
    }

}
