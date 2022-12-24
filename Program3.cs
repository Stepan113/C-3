Console.WriteLine("Введите число: ");
int num=Convert.ToInt32(Console.ReadLine());
for (int i=1;i<=num;i+=1)
{
    Console.WriteLine($"Куб {i} равен {i*i*i}");
}
