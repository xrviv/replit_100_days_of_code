print("Getting to know you!")
print()
name = input("What's your name?: ")
food = input("What's your favorite food: ")
music = input("What's your favorite music? ")
loc = input("Where do you live?: ")
print()
print("You are")
print(name)
print("You're probably hankering for")
print(food)
print("and you're definitely getting your groove on to")
print(music)
print("living in the amazing")
print(loc)
print()
print("""

In C++ this is a similar way to do it:
========
#include <iostream>
#include <string>

using namespace std;

int main(){
	string name;
	cout << "Please enter your name: " << flush;
    cin >> name;
    cout << "Hello, " << name << endl;
	return(0);
}

""")

print("""

In html/javascript this is a similar way to do it:
========

<!DOCTYPE html>
<html>
<body>

<input id="userinput"> <br>

<button onclick="greetings()"> Type your name and click </button>

<script>

function greetings() {
var name = document.getElementById("userinput").value;

document.write("Hello!!, " + name);
}


</script>

</body>
</html>


""")
