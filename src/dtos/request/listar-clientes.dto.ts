import { IsNumber, IsOptional, IsPositive } from "class-validator";
import { BaseDto } from "../base.dto";

export class ListarClienteDto extends BaseDto {
  @IsOptional()
  @IsNumber()
  @IsPositive()
  page: number;

  @IsOptional()
  @IsNumber()
  @IsPositive()
  perPage: number;
}
