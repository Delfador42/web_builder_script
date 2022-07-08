import React, { Component } from 'react';
import Pdf from '../files/b.pdf';
export default function Page1() {

      return (
          <div className = "pdf_container">
              <object data={Pdf} type="application/pdf" width="100%" height="100%"></object>
          </div>
        );
  }
  