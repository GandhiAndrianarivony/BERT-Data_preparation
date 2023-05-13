import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  form!: FormGroup;
  response: any;

  constructor(private fb: FormBuilder, private http: HttpClient) {
      this.form = this.fb.group({
        text: ['', Validators.required]
      });
  }

  ngOnInit(): void {
  }

  onSubmit(){
    const formData = this.form.value;

    const headers = {
      'Content-Type': 'application/json'
    };

    this.http.post('https://example.com/endpoint', JSON.stringify(formData), { headers }).subscribe(response => {
      this.response = response;
      console.log(response);
    }, error => {
      console.error(error);
    });
  }

}

