import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarsComponent } from './cars/cars.component';
import { ShowCarsComponent } from './cars/show-cars/show-cars.component';
import { CrudCarsComponent } from './cars/crud-cars/crud-cars.component';

const routes: Routes = [
  {path:'cars', component: CarsComponent},
  {path:'view-cars-on-sale', component: ShowCarsComponent},
  {path:'sale-car', component: CrudCarsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
