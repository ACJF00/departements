import React, { useState, useEffect } from "react";
import "./index.css";
import deps from "./deps.json";
import Confetti from "react-confetti";
import { FiChevronDown, FiChevronUp } from "react-icons/fi";
import { FiRefreshCcw } from "react-icons/fi";

function App() {
  const [currentDep, setCurrentDep] = useState(null);
  const [userChoice, setUserChoice] = useState("");
  const [isCorrect, setIsCorrect] = useState(null);
  const [showCorrect, setShowCorrect] = useState(false);
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });
  const [isSpoilerOpen, setIsSpoilerOpen] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  // Choisissez un département aléatoire au chargement de la page
  useEffect(() => {
    shuffleDep();
    setIsCorrect(null);
  }, []);

  const shuffleDep = () => {
    const randomDep = deps[Math.floor(Math.random() * deps.length)];
    console.log("RANDOM", randomDep);
    setCurrentDep(randomDep);
    console.log(randomDep);
    setIsSpoilerOpen(false); // Ajoutez cette ligne
  };

  const checkAnswer = () => {
    if (userChoice === currentDep.nom) {
      setIsCorrect(true);
      setIsCorrect(true);
      setShowCorrect(true);
      setTimeout(() => setShowCorrect(false), 3000);
      shuffleDep();
      setIsCorrect(null);
      setUserChoice("");
    } else {
      setIsCorrect(false);
    }
  };

  return (
    // <div>
    //   {currentDep.code}
    // </div>
    <div className="App flex flex-col min-h-screen bg-gray-50">
     {currentDep && currentDep.image && (
      <div className="h-40 lg:h-80 shadow-xl">
      <img src={`./images/${currentDep.image}`} alt="Hero" className="h-full w-full object-cover"></img>
    </div>
     )}

      <div className="flex flex-col w-fit mx-auto lg:m-auto items-center justify-center gap-4 text-center pt-10">
        {currentDep && (
          <>
            {showCorrect && (
              <div
                className="h-screen w-screen flex justify-center items-center absolute backdrop-blur-lg text-3xl text-green-500 font-bold transition transform duration-200 ease-out scale-100 opacity-100 z-50"
                onClick={() => setShowCorrect(false)}
              >
                <Confetti width={windowSize.width} height={windowSize.height} />
                Correct !
              </div>
            )}
            <p className="text-x font-bold">
              Quel est le nom du département numéro {currentDep.code} ?
            </p>
            <input
              list="dep-names"
              value={userChoice}
              onChange={(e) => setUserChoice(e.target.value)}
              placeholder="Réponse"
              className={`${
                isCorrect === true
                  ? "border-4 border-green-500"
                  : isCorrect === false
                  ? "border-4 border-red-500"
                  : ""
              }`}
            />
            <datalist id="dep-names">
              {deps.map((dep, index) => (
                <option key={index} value={dep.nom} />
              ))}
            </datalist>
            <div className="flex gap-4">
              <button onClick={checkAnswer} className="btn">
                Vérifier
              </button>
              <button onClick={shuffleDep} className="btn-outline">
                <FiRefreshCcw />
              </button>
            </div>

            <div
              className="cursor-pointer"
              onClick={() => setIsSpoilerOpen(!isSpoilerOpen)}>
              <div className="flex items-center gap-4">
                Réponse
                {isSpoilerOpen ? <FiChevronUp /> : <FiChevronDown />}
              </div>
              {isSpoilerOpen && (
                <div className="text-green-500 font-bold">{currentDep.nom}</div>
              )}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
