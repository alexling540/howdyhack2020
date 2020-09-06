import React from 'react';
import '../../App.css';
import Footer from '../Footer';

export default function face_rec() {

  return (
    <>
      <h1 >FACIAL RECOGNITION</h1>;

      <div className='par__container'>
        <form method='post' enctype='multipart/form-data'>
          <p>
            <input type='file' class='btn--medium' name='file' />
            <br />
            <br />
            <input type='submit' class='btn--medium' value='Upload' />

          </p>
        </form>
      </div>
      <Footer />
    </>
  );
}
