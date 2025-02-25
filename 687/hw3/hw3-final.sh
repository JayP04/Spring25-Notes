#!/system/bin/sh

# first to launch the app, we need monkey prompt
adb shell monkey -p com.example.h3 -c android.intent.category.LAUNCHER 1
sleep 3

# now i will create a tap function that will tap the 
# in an order that willl tap all possible combinations.


# I got this idea when i was looking through shell scripting.
# I intially wrote all the sequences but thought this would be better.
tap() {
    adb shell input tap $1
    sleep 2
    adb shell input tap $2
    sleep 2
    adb shell input tap $3
    sleep 2
}

# doing the tapping like this would be convinient.
# this could be done by a loop as well but thats too high-end code 
# I dont want to write all possible orders by myself thats why i am creating this

# sequences()
# tap $1 in function calls the first dimension 18 244 and so on...
tap "18 244" "380 244" "738 244"
tap "380 244" "738 244" "18 244"
tap "738 244" "18 244" "380 244"

tap "738 244" "380 244" "18 244"
tap "380 244" "18 244" "738 244"
tap "18 244" "738 244" "380 244"


# at last we close with force stop
adb shell am force-stop com.example.h3