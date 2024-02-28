#include <iostream>
#include <string>

using namespace std;

int main()
{
	cout << "Welcome on HackTools\n";
	while (true)
	{
		string cmd;
		cout << "Type a command\n";
		cin >> cmd;
		if (cmd == "/?") {
			cout << "\n/b -> Launch base converter. Take no arguments\n/c -> Clear the console. Take no arguments\n/o -> Close HackTools/console. Take no arguments\n/pg -> Launch Password Generator. Take no arguments\n/? -> Show all command with a explanation\n\n";
		
		} else if (cmd == "/c") {
			system("clear");
		
		} else if (cmd == "/b") {
			system("python /bin/hacktools/basor.py");
			
		} else if (cmd == "/pg") {
			system("python /bin/hacktools/pg.py");
			
		} else if (cmd == "/o") {
			break;
			
		} else {
			cout << "Sorry, unknown command\n";
		}
	}
	
	cout << "Bye\n";
	
	return 0;
}
