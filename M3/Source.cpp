#include <iostream>
#include <conio.h>
#include <random>

using namespace std;

void main()
{
	random_device device;
	mt19937 generator(device());
	uniform_int_distribution<int> liczby(1, 3);

	bool stop = false;
	float n, win, lose, stay, czejndz;
	n = win = lose = stay = czejndz = 0;

	do
	{
		system("cls");
		n++;
		int wygrana = liczby(generator);
		int wybor;
		int pusta;

		cout << "Wybierz numer bramki[1,2,3]";
		cin >> wybor;
		int tmp = wybor;
		bool check = false;

		do
		{
			pusta = liczby(generator);
			if (pusta != wygrana && pusta != wybor)
				check = true;
		} while (check != true);

		cout << "Pusta bramka: " << pusta << endl << wygrana << endl;

		if (pusta == 1)
			cout << "Wybierz numer bramki[2,3]: ";
		if (pusta == 2)
			cout << "Wybierz numer bramki[1,3]: ";
		if (pusta == 3)
			cout << "Wybierz numer bramki[1,2]: ";

		cin >> wybor;


		if (wybor == wygrana)
		{
			cout << "Wygrales  ";
			if (wybor == tmp)
			{
				stay++;
			}
			else
			{
				czejndz++;
			}
		}
		else
		{
			cout << "Przegrales  ";
		}
		
		char c;
		cout << endl << "Grasz dalej? [t/n] ";
		cin >> c;
		if (c == 'n')
		{
			stop = true;
		}
	} while (stop != true);
	
	cout << "Stats: " << endl << "Zmiana: " << 100*(czejndz / n) << "%" << endl << "Zostan: " << 100*(stay / n)<< "%";
	_getch();
 
}
