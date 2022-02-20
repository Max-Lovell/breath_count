Qualtrics.SurveyEngine.addOnload(function () {
    //https://api.qualtrics.com/api-reference/ZG9jOjg0MDczOA-api-reference
    var qthis = this;
    qthis.hideNextButton();

    var ini_time; //time start button is clicked
    var key_times = []; // stores key press timings since button click
    var keys_data = []; //stores participant trial data
    
    var raw_keys_screen = []; //stores key presses on practices
    var keys_screen = []; //tracks input for practice feedback
    
    function startTimer() { //when 'start button' is clicked
        ini_time = performance.now()
        document.getElementById('ini_button').disabled = true; //only allow one click
    
        //TIMER
        if(document.getElementById('timer_text').innerHTML === 'practice'){
            timer_length = 1
        } else {timer_length = 10}
        total_sec = (timer_length*60)-1
        
        timer_var = setInterval(function(){
            mins = parseInt(total_sec / 60, 10)
            secs = parseInt(total_sec % 60, 10)
            mins = mins < 10 ? '0' + mins : mins
            secs = secs < 10 ? '0' + secs : secs
            document.getElementById('timer').innerHTML = mins + ':' + secs
    
            if (--total_sec < 0){ //when it hits 0, change things
                clearInterval(timer_var)
                if(document.getElementById('timer_text').innerHTML === 'task'){ //END EXP
                    window.removeEventListener('keydown', keyListener)
                    window.removeEventListener('keyup', colour_keys)
                    let csvContent = keys_data.map(e => e.join(",")).join(",");
                    saveData(csvContent);
                    qthis.clickNextButton();
                    qthis.showNextButton();
                    jQuery("#NextButton").click();
                    return
                } else if(document.getElementById('timer_text').innerHTML === 'practice'){ //end prac
                    document.getElementById('key_presses').innerHTML = '';
                    document.getElementById('ini_button').disabled = false;
                    document.getElementById('timer_text').innerHTML = 'task';
                    document.getElementById('button_text').innerHTML = 'experiment';
                    document.getElementById('timer').innerHTML = '10:00';
                }
            }
        }, 1000)
        window.addEventListener('keydown', keyListener) //listen for key presses
        window.addEventListener('keyup', colour_keys)
    }

    function keyListener(e){ //to avoid global variables try: https://stackoverflow.com/questions/10000083/javascript-event-handler-with-parameters     
        if(e.repeat) { return } //stops holding the key down making repeat characters
        if(['ArrowDown','ArrowUp','ArrowLeft','ArrowRight',' '].includes(e.key)) { //https://stackoverflow.com/a/44213036/7705626
            e.preventDefault();//disable arrow key scrolling etc
        //if main trials calc rt and store in global variable
            if(document.getElementById('timer_text').innerHTML === 'task' && document.getElementById('ini_button').disabled === true){
                key_times.push(e.timeStamp) //may return getTime.now() level of accuracy on some browsers
                if(keys_data.length !== 0){
                    let last_time = key_times[key_times.length-2]; //timing of last key press
                    var reaction_time = e.timeStamp - last_time; //stores final reaction time
                } else { var reaction_time = e.timeStamp - ini_time } //on the first time
                keys_data.push([e.key,reaction_time.toString()]);
                colour_keys(e,'blue','red')
            }

        //PRACTICE
            if(document.getElementById('timer_text').innerHTML === 'practice'){
                var feedback_col;
                raw_keys_screen.push(e.key)
                if(e.key === ' '){
                    keys_screen = ['RESET']
                } else if (raw_keys_screen.length < 9){
                    if(e.key === 'ArrowUp' && raw_keys_screen.slice(0,raw_keys_screen.length-1).every(function(first8){return first8 === 'ArrowUp'})){
                        keys_screen.push(' Breath ' + raw_keys_screen.length)
                        feedback_col = 'green'
                    } else {
                        keys_screen = ['Incorrect breath sequence']
                        feedback_col = 'red'
                    }
                } else if (raw_keys_screen.length === 9){
                    if(e.key === 'ArrowDown'){
                        keys_screen.push(' Breath 9')
                        feedback_col = 'green'
                    } else {keys_screen = ['Incorrect breath sequence']
                            feedback_col = 'red'            
                    }
                } else if (raw_keys_screen.length === 10){
                    if(e.key === 'ArrowLeft'){
                        keys_screen.push(' Accuracy: Unsure')
                        feedback_col = 'green'
                    } else if (e.key ==='ArrowRight'){
                        keys_screen.push(' Accuracy: Confident')
                        feedback_col = 'green'
                    } else {keys_screen = ['Incorrect breath sequence']
                            feedback_col = 'red'
                    }
                }
                colour_keys(e,feedback_col,'red');
                document.getElementById('key_presses').innerHTML = keys_screen;
                if (raw_keys_screen.length === 10 || keys_screen[0] === 'Incorrect breath sequence' || keys_screen[0] === 'RESET'){
                    raw_keys_screen.length = 0
                    keys_screen.length = 0
                }
            } // end prac feedback function
    
        }
    }
    
    function colour_keys(key_pressed, arrow_col='black', break_col='black'){ //
        if (key_pressed.key === 'ArrowDown') {document.getElementById('down').style.color = arrow_col}
        if (key_pressed.key === 'ArrowUp') {document.getElementById('up').style.color = arrow_col}
        if (key_pressed.key === 'ArrowLeft') {document.getElementById('left').style.color = arrow_col}
        if (key_pressed.key === 'ArrowRight') {document.getElementById('right').style.color = arrow_col}
        if (key_pressed.key === ' ') {document.getElementById('space').style.color = break_col}
    }
    
    function saveData(dataset) {
        //var email = "${e://Field/RecipientEmail}";
        var sbj_id = "${e://Field/Random_ID}";
        jQuery.ajax({
            method: 'POST',
            dataType: 'json',
            cache: false,
            url: '[public_URL]/save_data.php',
            data: {
                file_name: sbj_id + "_breath_pre", //file_name: sbj_id + email + "_breath_post",
                exp_data: JSON.stringify(dataset)
            }
        });
    }
    
    document.getElementById('ini_button').onclick = startTimer;
})

Qualtrics.SurveyEngine.addOnReady(function(){});
Qualtrics.SurveyEngine.addOnUnload(function(){});
