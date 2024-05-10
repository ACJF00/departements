import React, { useState, useEffect } from 'react';
import "./index.css";
import deps from './deps.json';

function App() {
  const [currentDep, setCurrentDep] = useState(null);
  const [userChoice, setUserChoice] = useState('');

  // Choisissez un département aléatoire au chargement de la page
  useEffect(() => {
    shuffleDep();
  }, []);

  const shuffleDep = () => {
    const randomDep = deps[Math.floor(Math.random() * deps.length)];
    setCurrentDep(randomDep);
  };

  const checkAnswer = () => {
    if (userChoice === currentDep.nom) {
      alert('Correct !');
      shuffleDep();
      setUserChoice('');
    } else {
      alert('Incorrect, essayez encore.');
    }
  };

  return (
    <div className="App flex min-h-screen bg-gray-50">
        <div className="flex flex-col w-fit m-auto items-center justify-center gap-4 text-center">
      {currentDep && (
        <>
          <p className="text-xl">Quel est le nom du département numéro {currentDep.code} ?</p>
          <input list="dep-names" value={userChoice} onChange={e => setUserChoice(e.target.value)} placeholder="Réponse"/>
          <datalist id="dep-names">
            {deps.map((dep, index) => (
              <option key={index} value={dep.nom} />
            ))}
          </datalist>
          <button onClick={checkAnswer} className="btn">Vérifier</button>
          <button onClick={shuffleDep} className="btn-outline">Changer de département</button>
          <details className="cursor-pointer">
            <summary>Réponse</summary>
            <p>{currentDep.nom}</p>
          </details>
        </>
      )}
    </div>
    </div>
  );
}

export default App;