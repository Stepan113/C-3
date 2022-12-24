Console.WriteLine("Введите пятизначное число: ");
int num=Convert.ToInt32(Console.ReadLine());
if (num<100000 && num>-100000)
{
    if (num/10000==num%10 && num/1000%10==num%100/10)
    {
        Console.WriteLine($"Число {num} палиндром");
    }
    else
    {
        Console.WriteLine($"Число {num} не палиндром");
    }
}
else
{
    Console.WriteLine("Число не пятизначное");
}
