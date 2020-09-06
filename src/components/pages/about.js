import React from 'react';
import '../../App.css';

import '../Cards.css';
import CardItem from '../CardItem';

import Footer from '../Footer';
import Paragraphs from '../Paragraphs'


export default function About() {
  return (
    <>
      <h1 className='about'>ABOUT</h1>;

      <Paragraphs />

      <div className='cards'>
        <h1>Meet the Team</h1>
        <div className='cards__container'>
          <div className='cards__wrapper'>
            <ul className='cards__items'>
              <CardItem
                src='images/dan.jpg'
                text='Daniel Chamorro'
                label='Front-End'
                path='/'
              />
              <CardItem
                src='images/bryce.jpg'
                text='Bryce Bodner'
                label='Python'
                path='/services'
              />
              <CardItem
                src='images/img-9.jpg'
                text='Alex Ling' 
                label='Back-end'
                path='/products'
              />
              <CardItem
                src='images/apsara.jpg'
                text='Apsara Mitra'
                label='Front-end'
                path='/sign-up'
              />
            </ul>
          </div>
        </div>
      </div>



      
      <Footer />
    </>
  );
}
