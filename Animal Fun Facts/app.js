import { animals } from './animals';
import React from 'react';
import ReactDOM from 'react-dom';

const title = "";
const showBackground = true;
const background = <img className='background' alt='ocean' src='./images/ocean.jpg' />;
const images = [];
for (const animal in animals) {
    images.push(<img onClick={displayFact} key={animal} className='animal' alt={animal} src={animals[animal].image} aria-label={animal} role='button' />)
};
const animalFacts = (
    <div>
        {showBackground && background}
        <p id='fact'></p>
        <div className='animals'>
            {images}
        </div>
        <h1>{title || 'Click an animal for a fun fact'}</h1>
    </div>
);
ReactDOM.render(animalFacts, document.getElementById('root'));

function displayFact(e) {
    let animal = e.target.alt;
    let randIndex = Math.floor(Math.random() * animals[animal].facts.length);
    let funFact = animals[animal].facts[randIndex];
    document.getElementById('fact').innerHTML = funFact;
}
