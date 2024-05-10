import React, { useState, useEffect } from 'react';
import "./index.css";
import deps from './deps.json';
import Confetti from 'react-confetti';

function App() {
  const [currentDep, setCurrentDep] = useState(null);
  const [userChoice, setUserChoice] = useState('');
  const [isCorrect, setIsCorrect] = useState(null);
  const [showCorrect, setShowCorrect] = useState(false);
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });
  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);
  // Choisissez un département aléatoire au chargement de la page
  useEffect(() => {
    shuffleDep();
    setIsCorrect(null);
  }, []);

  const shuffleDep = () => {
    const randomDep = deps[Math.floor(Math.random() * deps.length)];
    setCurrentDep(randomDep);
  };

  const checkAnswer = () => {
    if (userChoice === currentDep.nom) {
      setIsCorrect(true);
      setIsCorrect(true);
      setShowCorrect(true);
      setTimeout(() => setShowCorrect(false), 3000);
      shuffleDep();
      setIsCorrect(null);
      setUserChoice('');
    } else {
      setIsCorrect(false);
    }
  };

  return (
    <div className="App flex min-h-screen bg-gray-50">
        <div className="flex flex-col w-fit m-auto items-center justify-center gap-4 text-center">
      {currentDep && (
        <>
          {showCorrect && (
            <div 
              className="h-screen w-screen flex justify-center pt-24 absolute backdrop-blur-lg text-3xl text-green-500 font-bold transition transform duration-200 ease-out scale-100 opacity-100"
              onClick={() => setShowCorrect(false)} // Ajoutez cette ligne
            >
              <Confetti
                width={windowSize.width}
                height={windowSize.height}
              />
              Correct !
            </div>
          )}
          <p className="text-x font-bold">Quel est le nom du département numéro {currentDep.code} ?</p>
          <input list="dep-names" value={userChoice} onChange={e => setUserChoice(e.target.value)} placeholder="Réponse"
             className={`${isCorrect === true ? 'border-4 border-green-500' : isCorrect === false ? 'border-4 border-red-500' : ''}`}
          />
          <datalist id="dep-names">
            {deps.map((dep, index) => (
              <option key={index} value={dep.nom} />
            ))}
          </datalist>
          <button onClick={checkAnswer} className="btn">Vérifier</button>
          <button onClick={shuffleDep} className="btn-outline">Changer de département</button>
          <details className="cursor-pointer">
            <summary>Réponse</summary>
            <p className="text-green-500 font-bold">{currentDep.nom}</p>
          </details>
        </>
      )}
    </div>
    </div>
  );
}

export default App;