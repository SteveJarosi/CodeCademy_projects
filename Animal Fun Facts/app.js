import { animals } from './animals';
import React from 'react';
import ReactDOM from 'react-dom';

const title = "";
const background = <img className='background' alt='ocean' src='/images/ocean.jpg'/>
const images = [];
for (const animal in animals) {
  images.push(<img key={animal} className='animal' alt={animal} src= {animals[animal].image} aria-label={animal} role='button' />)
};
//console.log(images);
const animalFacts = (
  <div>
  {background}
  <div className='animals'>
  {images}
  </div>
  <h1>{title ? title : 'Click an animal for a fun fact'}</h1>
  </div>
);
ReactDOM.render(animalFacts, document.getElementById('root'));

