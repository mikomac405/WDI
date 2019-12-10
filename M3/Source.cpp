#include <iostream>
#include <random>
#include <conio.h>

using namespace std;

void play();
void simulate(int);

random_device device;
mt19937 generator(device());
uniform_int_distribution<int> liczby(1, 3);

bool stop = false;
float n{}, win{}, lose{}, stay{}, change{};

int main() {
	play();
	simulate(100000);
	_getch();
	return 0;
}

void play() {
	do {
		n++;
		int wygrana = liczby(generator);;
		int wybor;
		int pusta;

		cout << "Wybierz numer bramki[1,2,3]" << endl;
		cin >> wybor;
		int tmp = wybor;
		bool check = false;

		do {
			pusta = liczby(generator);
			if (pusta != wygrana && pusta != wybor)
				check = true;
		} while (check != true);

		cout << "Pusta bramka: " << pusta << endl;

		if (pusta == 1)
			cout << "Wybierz numer bramki[2,3]: ";
		if (pusta == 2)
			cout << "Wybierz numer bramki[1,3]: ";
		if (pusta == 3)
			cout << "Wybierz numer bramki[1,2]: ";

		cin >> wybor;

		if (wybor == pusta) {
			cout << "Wybrales zla bramke." << endl;
			n--;
			continue;
		}

		if (wybor == wygrana) {
			cout << "Wygrales!" << endl;
			if (wybor == tmp) {
				stay++;
			}
			else {
				change++;
			}
		}
		else {
			cout << "Pudlo!" << endl;
			if (wybor == tmp) {
				change++;
			}
			else {
				stay++;
			}
		}

		cout << "Statystki: " << endl << "Zmiana: " << 100 * (change / n) << "%" << endl << "Pozostanie: "
			<< 100 * (stay / n) << "%";

		char c;
		cout << endl << "Grasz dalej? [t/n] " << endl;
		cin >> c;
		if (c == 'n') {
			stop = true;
		}
	} while (stop != true);
}

void simulate(int counter) {
	cout << "Przeprowadzmy symulacje " << counter << " raz(y)" << endl;
	bool switcher{};
	for (int i = 1; i <= counter; i++) {
		n++;
		int wygrana = liczby(generator);
		int wybor = liczby(generator);
		int pusta;
		int tmp = wybor;

		bool check = false;
		do {
			pusta = liczby(generator);
			if (pusta != wygrana && pusta != wybor)
				check = true;
		} while (check != true);

		check = false;
		if (switcher) {
			do {
				wybor = liczby(generator);
				if (wybor != pusta && pusta != tmp)
					check = true;
			} while (check != true);
		}
		switcher = !switcher;

		if (wybor == wygrana) {
			if (wybor == tmp) {
				stay++;
			}
			else {
				change++;
			}
		}
		else {
			if (wybor == tmp) {
				change++;
			}
			else {
				stay++;
			}
		}
	}
	cout << "Statystki: " << endl << "Zmiana: " << 100 * (change / n) << "%" << endl << "Pozostanie: "
		<< 100 * (stay / n) << "%";
}
