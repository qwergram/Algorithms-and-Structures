using System.Collections.Generic;

namespace mergesort
{
    class Program
    {   
        static List<int> Mergesort(List<int> array)
        {
            if (array.Count > 1)
            {
                var result = new List<int>();
                var first_half = new List<int>();
                var second_half = new List<int>();
                for (int i=0; i < array.Count; i++)
                {
                    if (i >= array.Count / 2)
                    {
                        second_half.Add(array[i]);
                    } else
                    {
                        first_half.Add(array[i]);
                    }
                }
                first_half = Mergesort(first_half);
                second_half = Mergesort(second_half);

                while (first_half.Count > 0 || second_half.Count > 0)
                {
                    if (first_half.Count == 0 && second_half.Count > 0)
                    {
                        result.Add(second_half[0]);
                        second_half.RemoveAt(0);
                    } else if (second_half.Count == 0 && first_half.Count > 0)
                    {
                        result.Add(first_half[0]);
                        first_half.RemoveAt(0);
                    } else if (first_half[0] < second_half[0])
                    {
                        result.Add(first_half[0]);
                        first_half.RemoveAt(0);
                    } else
                    {
                        result.Add(second_half[0]);
                        second_half.RemoveAt(0);
                    }
                }
                return result;
            }
            return array;
        }
    }
    
}
