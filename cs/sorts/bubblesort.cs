using System.Collections.Generic;

namespace bubblesort
{
    class Program
    {
        static List<int> Bubblesort(List<int> array)
        {
            int tmp;
            if (array.Count > 1)
            {
                for (int i=0; i < array.Count; i++)
                {
                    for (int j=1; j < array.Count; j++)
                    {
                        if (array[j-1] > array[j]) {
                            tmp = array[j - 1];
                            array[j - 1] = array[j];
                            array[j] = tmp;
                        }
                    }
                }
            }
            return array;
        }
    }
}
