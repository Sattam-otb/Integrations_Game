from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '1632'  # مفتاح سري لجلسات Flask

قوانين_التكامل = {
    "∫ sin(x) dx": "-cos(x)",
    "∫ cos(x) dx": "sin(x)",
    "∫ sec^2(x) dx": "tan(x)",
    "∫ csc^2(x) dx": "-cot(x)",
    "∫ sec(x)tan(x) dx": "sec(x)",
    "∫ csc(x)cot(x) dx": "-csc(x)"
}
الدوال = list(قوانين_التكامل.keys())
عدد_الأسئلة = 5

@app.route('/')
def ابدأ_اللعبة():
    session.clear()
    session['نقاط'] = 0
    session['سؤال_رقم'] = 0
    return عرض_السؤال()

@app.route('/question')
def عرض_السؤال():
    if session['سؤال_رقم'] < عدد_الأسئلة:
        session['سؤال_حالي'] = random.choice(الدوال)
        session['الإجابة_صحيحة'] = قوانين_التكامل[session['سؤال_حالي']]
        خيارات_إجابات = [session['الإجابة_صحيحة']]
        while len(خيارات_إجابات) < 4:
            إجابة_خاطئة = random.choice(list(قوانين_التكامل.values()))
            if إجابة_خاطئة not in خيارات_إجابات:
                خيارات_إجابات.append(إجابة_خاطئة)
        random.shuffle(خيارات_إجابات)
        session['خيارات'] = خيارات_إجابات
        session['سؤال_رقم'] += 1
        return render_template('index.html', question=session['سؤال_حالي'], options=session['خيارات'], score=session['نقاط'], question_number=session['سؤال_رقم'], total_questions=عدد_الأسئلة)
    else:
        return render_template('result.html', score=session['نقاط'], total_questions=عدد_الأسئلة)

@app.route('/check_answer', methods=['POST'])
def فحص_الإجابة():
    إجابة_المستخدم = request.form['answer']
    if إجابة_المستخدم == session['الإجابة_صحيحة']:
        session['نقاط'] += 1
        return jsonify({'result': 'correct', 'score': session['نقاط']})
    else:
        return jsonify({'result': 'incorrect', 'correct_answer': session['الإجابة_صحيحة'], 'score': session['نقاط']})

if __name__ == '__main__':
    from flask import session
    app.run(debug=True)