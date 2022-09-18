import { Component, Inject, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-cars',
  templateUrl: './show-cars.component.html',
  styleUrls: ['./show-cars.component.css']
})
export class ShowCarsComponent implements OnInit {
  
  carsList:any = [];
  

  constructor(private service:SharedService) { 
  }

  ngOnInit(): void {
    this.refreshCarList();

  }

  refreshCarList(){
    this.service.getAll().subscribe(data=>{
      this.carsList = data;
    });
  }

}
