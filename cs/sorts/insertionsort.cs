using System.Collections.Generic;

namespace insertionsort
{
    class Program
    {
        static List<int> InsertionSort(List<int> values)
        {
            if (values.Count > 1)
            {
                int tmp;
                for (int j=0; j < values.Count - 1; j++)
                {
                    for (int i=1; i < values.Count; i++)
                    {
                        if (values[i] < values[i-1])
                        {
                            tmp = values[i];
                            values[i] = values[i - 1];
                            values[i - 1] = tmp;
                        }
                    }
                }
            }
            return values;
        }
    }
}
